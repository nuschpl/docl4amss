#!/usr/bin/env python
"""
use gdb protocol to act as jtag console to okl4

gdb proto implemention is quick and hackish

---
to run okl4 from "elf" file:
 $ qemu-system-arm -M versatileab -s -S -kernel elf -m 512 \
       -curses -monitor stdio 

(XXX will crash in quartz unless you use tools/sortelf.py
on your elf binary.)

then in another window run this program:
 $ ./cons-gdb.py


notes:
   http://davis.lbl.gov/Manuals/GDB/gdb_31.html
"""

import socket, sys

class Error(Exception) : pass

def pkt(d) :
    """gdb packet"""
    s = sum(ord(ch) for ch in d) & 0xff
    return '$%s#%02x' % (d, s)

def unrle(r) :
    while '*' in r :
        x = r.index('*')
        c = ord(r[x+1]) - 29
        r = r[:x] + r[x-1] * c + r[x+2:]
    return r

def unpkt(p) :
    if p[0] != '$' or p[-3] != '#' :
        raise Error('bad format')
    d = p[1:-3]
    s = sum(ord(ch) for ch in d) & 0xff
    if s != int(p[-2:], 16) :
        raise Error('bad cksum')
    return unrle(d)

def getPkt(s) :
    r = []
    while len(r) < 3 or r[-3] != '#' :
        ch = s.recv(1)
        if not ch :
            raise Error('eof')
        r.append(ch)
        if r[0] != '$' :
            raise Error('bad format')
    return unpkt(''.join(r))

def sendCmd(s, d) :
    s.send(pkt(d))
    ch = s.recv(1)
    if ch != '+' :
        raise Error("bad ack")
    return getPkt(s)

def cont(s, addr=None) :
    if addr :
        return sendCmd(s, 'c%x' % addr)
    return sendCmd(s, 'c')

def bpt(s, addr) :
    return sendCmd(s, "Z1,%x,4" % addr)

def unbpt(s, addr) :
    return sendCmd(s, "z1,%x,4" % addr)

def lehex(v) :
    return ''.join('%02x' % ((v >> n) & 0xff) for n in [0,8,16,24])

def unlehex(v) :
    if len(v) != 8 :
        raise Error('bad lehex: %r' % v)
    return int(v[0:2], 16) | (int(v[2:4], 16) << 8) | (int(v[4:6], 16) << 16) | (int(v[6:8], 16) << 24) 

def setRegs(s, vs) :
    vstr = ''.join(lehex(v) for v in vs)
    return sendCmd(s, 'G%s' % vstr)

def setReg(s, r, v) :
    vs = getRegs(s)
    vs[r] = v
    return setRegs(s, vs)

def splitn(s, n) :
    return [s[p : p + n] for p in xrange(0, len(s), n)]

def getRegs(s) :
    x = sendCmd(s, 'g');
    return [unlehex(v) for v in splitn(x, 8)]

def getReg(s, r) :
    return getRegs(s)[r]

def getBytes(s, addr, l) :
    x = sendCmd(s, 'm%x,%x' % (addr, l))
    return [int(x[n:n+2],16) for n in xrange(0, len(x), 2)]
    
def getHalfs(s, addr, l) :
    bs = getBytes(s, addr, 2*l)
    return [(bs[n] | (bs[n+1]<<8)) for n in xrange(0, len(bs), 2)]

def getWords(s, addr, l) :
    x = sendCmd(s, 'm%x,%x' % (addr, 4*l))
    return [unlehex(v) for v in splitn(x, 8)]

def putWords(s, addr, vs) :
    mem = ''.join(lehex(v) for v in vs)
    return sendCmd(s, 'M%x,%x:%s' % (addr, 4*len(vs), mem))

def getCStr(s, addr) :
    r = []
    while addr :
        ch = getBytes(s, addr, 1)[0]
        addr += 1
        if ch == 0 :
            break
        r.append(chr(ch))
    return ''.join(r)

def step(s) :
    return sendCmd(s, 's')

def kill(s) :
    s.send(pkt('k'))

def connect(port=1234) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', port))
    return s

def stepBpt(s, addr) :
    unbpt(s, addr)
    step(s)
    bpt(s, addr)

def getCh() :
    """Get char in raw mode."""
    import tty, termios
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)
    try :
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally :
        termios.tcsetattr(fd, termios.TCSADRAIN, orig)
    return ch

def runCons() :
    PC=15
    LR=14
    SP=13
    
    GETC = 0xf000f3f8
    PUTC = 0xf000f3bc
    ERR = 0x16E42D4C
    ERR2 = 0x16E43024
    LOG = 0x00B0CEC0
    
    s = connect()
    print bpt(s, GETC)
    print bpt(s, PUTC)
    print bpt(s, ERR)
    print bpt(s, ERR2)
    print bpt(s, LOG)

    # XXX
    #print putWords(s, 0x01f000c0, [1])  # heap init in smem
    
    try :
        while 1 :
            cont(s)
            reg = getRegs(s)
            if reg[PC] == PUTC :
                sys.stdout.write(chr(reg[0]))
                sys.stdout.flush()
            elif reg[PC] == GETC :
                ch = getCh()
                if ch in ['', '\x03', '\x04'] : # eof, ^c or ^d quits
                    break
                reg[0] = ord(ch)
                reg[PC] = reg[LR]
                setRegs(s, reg)
                continue

            elif reg[PC] in [ERR, ERR2] :
                print '%x - Err: %d line %r %r @ 0x%08x' % (reg[PC], reg[0], getCStr(s, reg[1]), getCStr(s, reg[2]), reg[LR])

            elif reg[PC] == LOG :
                ws = getWords(s, reg[0], 5)
                print '%x - Debug: %d %d %r %r %d @ 0x%08x' % (reg[PC], ws[0], ws[1], getCStr(s, ws[2]), getCStr(s, ws[3]), ws[4], reg[LR])
        
            else :
                print 'done at %x' % reg[PC]
                break
            stepBpt(s, reg[PC])
    except Error, e :    
        print 'exception: %r' % e
    except KeyboardInterrupt :
        pass
    finally :
        print 'done...'
        kill(s)
    
runCons()

