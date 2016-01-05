# OKL4 kernel #

OkL4 is a microkernel in the L4 family. It descends from the Pistachio L4 kernel by way of NICTA. The version of the kernel used in the Qualcomm baseband is based on a version that is newer than the latest NICTA release (iguana-project--devel--1.1--version-0) and older than the oldest version
provided by OK-Labs (Okl4\_release\_1.4.1.1).
Okl4\_release\_1.4.1.1 version is the
closest known public release.
OkL4 is pared with Iguana
to provide additional operating system services on top of the
sparse L4 kernel.

The same OkL4 and Iguana images are used in all known
radio images (with minor variations in the boot info
structure to account for different sizes of other
program sections linked together with the kernel).
The Kernel Information Page for these images is:

```
Kernel Interface Page:
  Magic            L4�K
  API version      0x86.0x04
  API flags        little-endian, 32-bit
  Space info       num spaces: 1
  VirtualReg info  num mrs: 32
  UTCB area info   min size: 0KB, alignment: 256, UTCB size: 256
  KIP area info    min size: 0KB
  Boot info        0xa38000
  Clock info       scheduler precision 0 us
  Thread info      user base: 0x000, system base: 0x000, thread bits: 13
  Page info        sizes: 4K 64K 1M , rights: w

Root server:
  root server:    ip: 0xb0000000, sp: 0xb0000000, 0x00a61000:0x00ab8fff 
Kernel descriptor (160):
  Kernel ID        5.2
  Kernel gen date  2000 1, 1
  Kernel version   0.0.0
  Kernel supplier  NICT
  Version string   OKL4 - (provider: Open Kernel Labs) built on Dec 20 2007 17:3
0:29 using gcc version 3.4.4.
  Features         PIDs
                   virtualspaceids

System call offsets:
  MapControl       0x00000000    SpaceControl      0x00000000
  ThreadControl    0x00000000    ProcessorControl  0x00000000
  Ipc              0x00000000    Lipc              0x00000000
  CacheControl     0x00000000    ExchangeRegister  0x00000000
  Schedule         0x00000000    ThreadSwitch      0x00000000

Processors 1:
  Proc   0:      external freq = 0MHz, internal freq = 0MHz

Memory regions (15/97) (1f0):
  Physical:     0x00a26000 - 0x00a60bff   bootloader  0x0
                0x00b07000 - 0x01e4bfff   bootloader  0x0
                0x16e00000 - 0x17c573ff   bootloader  0x0
                0x00a70000 - 0x00aeffff   kernel heap
                0x00a61000 - 0x00a6f3ff   bootloader  0x0
                0x00a61000 - 0x00a6f3ff   initial mapping  0x0
                0x00af0000 - 0x00b06fff   bootloader  0x0
                0x00af0000 - 0x00b06fff   initial mapping  0x1
                0x00a38000 - 0x00a3dfff   bootloader  0x0
                0x00a26000 - 0x00a60bff   bootloader  0x0
                0x00b07000 - 0x01e4bfff   bootloader  0x0
                0x16e00000 - 0x17c573ff   bootloader  0x0
                0x00a38000 - 0x00a39fff   bootloader  0x0

  Virtual :     0xb0000000 - 0xb000e3ff   initial mapping  0x0
                0xb0040000 - 0xb0056fff   initial mapping  0x1
```

Note, if this had been an OKL4-1.4.1.1 image the supplier
would have been "OKL4" not "NICT" and if
it had been from the earlier NICTA iguana release it
would have an email address in the version string instead
of "provider: ...".
The accompanying bootinfo structure (used by iguana)
has a magic number of 0x1960021d with a version of 1.
The NICTA iguana release had no bootinfo structure
and the OKL4-1.4.1.1 release used a version of 2.
The API version 0x86 indicates NICTA N1 rev 4 (versus
API 0xa0 rev 2 for OKL4 1.4.4). The kernel ID
is 5.2 vs. 5.1 for NICTAs pistachio and 6.1 for
OKL4 1.4.1.1.


## Iguana ##
The KIP is configured to load Iguana as its root server.
Iguana provides servers and libraries to provide
common operating system services on top of L4.
All of the programs cooperating
with iguana share a common address space even though
they have different memory protection settings (ie.
the same data will always be accessed by the same
address from all the programs, although some programs
may not be able to read or write all addresses).
Iguana's libraries make it easier to define clients
and servers that communicate over L4's IPC mechanism
by providing an compiler for an interface definition
language. The compiler generates convenient stub
functions for clients and servers for each interface
function.

During startup, Iguana processes an embedded boot
script. The boot script in one of the radio images is
shown below; the script in other images is fairly similar.
(Note the fields in the dump are not all properly aligned
due to differences in the bootinfo structure in
the radio image and the closest known public release).

```
Iguana BoofInfo Operations:
HEADER (magic: 0x1960021d, version: 0x1, debug: 0x0)
ADD VIRT MEM (pool: 0x18000000, base: 0x7fffffff, end: 0x0)
ADD PHYS MEM (pool: 0x17c03000, base: 0x17ffffff, end: 0x0)
ADD VIRT MEM (pool: 0x80100000, base: 0xafffffff, end: 0x0)
ADD PHYS MEM (pool: 0x1e5c000, base: 0x1efffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0e04000, base: 0xbfffffff, end: 0x0)
ADD PHYS MEM (pool: 0xa3e000, base: 0xa3ffff, end: 0x0)
ADD VIRT MEM (pool: 0x2000000, base: 0xfffffff, end: 0x0)
ADD PHYS MEM (pool: 0xb06fff, base: 0xb06fff, end: 0x0)
ADD VIRT MEM (pool: 0x10100000, base: 0x16dfffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0321000, base: 0xb0cfffff, end: 0x0)
ADD VIRT MEM (pool: 0x0, base: 0x8fffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0d02000, base: 0xb0dfffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0141000, base: 0xb01fffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0241000, base: 0xb02fffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0057000, base: 0xb00fffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0107000, base: 0xb013ffff, end: 0x0)
ADD VIRT MEM (pool: 0xb0209000, base: 0xb023ffff, end: 0x0)
ADD VIRT MEM (pool: 0xb000f000, base: 0xb003ffff, end: 0x0)
NEW MS (owner: 0, base: 0xb0d00000, size: 0x2000, flags 0x12, attr: 0x0) = 1
MAP (vaddr: 0xb0d00000, size: 0x2000, paddr: 0xa38000)
NEW MS (owner: 0, base: 0xb0e00000, size: 0x4000, flags 0x12, attr: 0x0) = 2
MAP (vaddr: 0xb0e00000, size: 0x4000, paddr: 0xa3a000)

NEW PD (owner: 0) = 3
NEW THREAD (owner: 3, ip: 0xb0100000, priority: 200, name: "ig_n") = 4
NEW MS (owner: 3, base: 0x0, size: 0x1000, flags 0x1, attr: 0x0) = 5
ATTACH (pd: 3, ms: 5, rights: 0x7)
GRANT (pd: 3, obj: 5, rights: 0x7)
REGISTER CALLBACK (pd: 3, ms: 5)
NEW MS (owner: 3, base: 0x0, size: 0x1000, flags 0x1, attr: 0x0) = 6
ATTACH (pd: 3, ms: 6, rights: 0x7)
GRANT (pd: 3, obj: 6, rights: 0x7)
NEW MS (owner: 3, base: 0x0, size: 0x4000, flags 0x1, attr: 0x0) = 7
ATTACH (pd: 3, ms: 7, rights: 0x7)
GRANT (pd: 3, obj: 7, rights: 0x7)
REGISTER STACK (thread: 4, ms: 7)
REGISTER SERVER (thread: 4, ms: 7)
EXPORT (thread: 4, obj: 4096, local_key: 6, type: 1)
EXPORT (thread: 4, obj: 6, local_key: 5, type: 3)
EXPORT (thread: 4, obj: 7, local_key: 4, type: 2)
EXPORT (thread: 4, obj: 5, local_key: 7, type: 3)
NEW MS (owner: 3, base: 0xb0100000, size: 0x7000, flags 0x12, attr: 0x0) = 8
MAP (vaddr: 0xb0100000, size: 0x7000, paddr: 0xa26000)
ATTACH (pd: 3, ms: 8, rights: 0x5)
GRANT (pd: 3, obj: 8, rights: 0x5)
REGISTER SERVER (thread: 4, ms: 8)
NEW MS (owner: 3, base: 0xb0140000, size: 0x1000, flags 0x12, attr: 0x0) = 9
MAP (vaddr: 0xb0140000, size: 0x1000, paddr: 0xa2d000)
ATTACH (pd: 3, ms: 9, rights: 0x6)
GRANT (pd: 3, obj: 9, rights: 0x6)
REGISTER SERVER (thread: 4, ms: 9)
EXPORT (thread: 4, obj: 7, local_key: 256, type: 3)
ATTACH (pd: 3, ms: 2, rights: 0x7)
GRANT (pd: 3, obj: 2, rights: 0x7)
EXPORT (thread: 4, obj: 2, local_key: 8, type: 3)
RUN THREAD (name: 4)

NEW PD (owner: 0) = 10
NEW THREAD (owner: a, ip: 0xb0200000, priority: 150, name: "qdms") = 11
NEW MS (owner: 10, base: 0x0, size: 0x1000, flags 0x1, attr: 0x0) = 12
ATTACH (pd: 10, ms: 12, rights: 0x7)
GRANT (pd: 10, obj: 12, rights: 0x7)
REGISTER CALLBACK (pd: 10, ms: 12)
NEW MS (owner: 10, base: 0x0, size: 0x20000, flags 0x1, attr: 0x0) = 13
ATTACH (pd: 10, ms: 13, rights: 0x7)
GRANT (pd: 10, obj: 13, rights: 0x7)
NEW MS (owner: 10, base: 0x0, size: 0x4000, flags 0x1, attr: 0x0) = 14
ATTACH (pd: 10, ms: 14, rights: 0x7)
GRANT (pd: 10, obj: 14, rights: 0x7)
REGISTER STACK (thread: 11, ms: 14)
EXPORT (thread: 11, obj: 131072, local_key: 6, type: 1)
EXPORT (thread: 11, obj: 13, local_key: 5, type: 3)
EXPORT (thread: 11, obj: 14, local_key: 4, type: 2)
EXPORT (thread: 11, obj: 12, local_key: 7, type: 3)
NEW MS (owner: 10, base: 0xb0200000, size: 0x9000, flags 0x12, attr: 0x0) = 15
MAP (vaddr: 0xb0200000, size: 0x9000, paddr: 0xa2e000)
ATTACH (pd: 10, ms: 15, rights: 0x5)
GRANT (pd: 10, obj: 15, rights: 0x5)
NEW MS (owner: 10, base: 0xb0240000, size: 0x1000, flags 0x12, attr: 0x0) = 16
MAP (vaddr: 0xb0240000, size: 0x1000, paddr: 0xa37000)
ATTACH (pd: 10, ms: 16, rights: 0x6)
GRANT (pd: 10, obj: 16, rights: 0x6)
EXPORT (thread: 11, obj: 7, local_key: 256, type: 3)
ATTACH (pd: 10, ms: 2, rights: 0x7)
GRANT (pd: 10, obj: 2, rights: 0x7)
EXPORT (thread: 11, obj: 2, local_key: 8, type: 3)
RUN THREAD (name: 11)

NEW PD (owner: 0) = 17
NEW THREAD (owner: 11, ip: 0xb0300000, priority: 150, name: "quar") = 18
NEW MS (owner: 17, base: 0x0, size: 0x1000, flags 0x1, attr: 0x0) = 19
ATTACH (pd: 17, ms: 19, rights: 0x7)
GRANT (pd: 17, obj: 19, rights: 0x7)
REGISTER CALLBACK (pd: 17, ms: 19)
NEW MS (owner: 17, base: 0x0, size: 0x8000, flags 0x1, attr: 0x0) = 20
ATTACH (pd: 17, ms: 20, rights: 0x7)
GRANT (pd: 17, obj: 20, rights: 0x7)
NEW MS (owner: 17, base: 0x0, size: 0x4000, flags 0x1, attr: 0x0) = 21
ATTACH (pd: 17, ms: 21, rights: 0x7)
GRANT (pd: 17, obj: 21, rights: 0x7)
REGISTER STACK (thread: 18, ms: 21)
EXPORT (thread: 18, obj: 32768, local_key: 6, type: 1)
EXPORT (thread: 18, obj: 20, local_key: 5, type: 3)
EXPORT (thread: 18, obj: 21, local_key: 4, type: 2)
EXPORT (thread: 18, obj: 19, local_key: 7, type: 3)
NEW MS (owner: 17, base: 0xb0300000, size: 0x21000, flags 0x12, attr: 0x0) = 22
MAP (vaddr: 0xb0300000, size: 0x21000, paddr: 0xa40000)
ATTACH (pd: 17, ms: 22, rights: 0x7)
GRANT (pd: 17, obj: 22, rights: 0x7)
EXPORT (thread: 18, obj: 7, local_key: 256, type: 3)
ATTACH (pd: 17, ms: 2, rights: 0x7)
GRANT (pd: 17, obj: 2, rights: 0x7)
EXPORT (thread: 18, obj: 2, local_key: 8, type: 3)
RUN THREAD (name: 18)
NEW MS (owner: 0, base: 0x1f00000, size: 0x100000, flags 0x20, attr: 0x6) = 23
NEW MS (owner: 0, base: 0x10000000, size: 0x100000, flags 0x20, attr: 0x2) = 24
NEW MS (owner: 0, base: 0x900000, size: 0x100000, flags 0x20, attr: 0x2) = 25
NEW MS (owner: 0, base: 0x80000000, size: 0x100000, flags 0x20, attr: 0x2) = 26

NEW PD (owner: 0) = 27
NEW THREAD (owner: 1b, ip: 0xb07000, priority: 150, name: "AMSS") = 28
NEW MS (owner: 27, base: 0x0, size: 0x1000, flags 0x1, attr: 0x0) = 29
ATTACH (pd: 27, ms: 29, rights: 0x7)
GRANT (pd: 27, obj: 29, rights: 0x7)
REGISTER CALLBACK (pd: 27, ms: 29)
NEW MS (owner: 27, base: 0x0, size: 0x80000, flags 0x1, attr: 0x0) = 30
ATTACH (pd: 27, ms: 30, rights: 0x7)
GRANT (pd: 27, obj: 30, rights: 0x7)
NEW MS (owner: 27, base: 0x0, size: 0x10000, flags 0x1, attr: 0x0) = 31
ATTACH (pd: 27, ms: 31, rights: 0x7)
GRANT (pd: 27, obj: 31, rights: 0x7)
REGISTER STACK (thread: 28, ms: 31)
EXPORT (thread: 28, obj: 524288, local_key: 6, type: 1)
EXPORT (thread: 28, obj: 30, local_key: 5, type: 3)
EXPORT (thread: 28, obj: 31, local_key: 4, type: 2)
EXPORT (thread: 28, obj: 29, local_key: 7, type: 3)
NEW MS (owner: 27, base: 0xb07000, size: 0x3000, flags 0x12, attr: 0x0) = 32
MAP (vaddr: 0xb07000, size: 0x3000, paddr: 0xb07000)
ATTACH (pd: 27, ms: 32, rights: 0x5)
GRANT (pd: 27, obj: 32, rights: 0x5)
NEW MS (owner: 27, base: 0xb0a000, size: 0x900000, flags 0x12, attr: 0x0) = 33
MAP (vaddr: 0xb0a000, size: 0x900000, paddr: 0xb0a000)
ATTACH (pd: 27, ms: 33, rights: 0x5)
GRANT (pd: 27, obj: 33, rights: 0x5)
NEW MS (owner: 27, base: 0x140a000, size: 0xa52000, flags 0x12, attr: 0x0) = 34
MAP (vaddr: 0x140a000, size: 0xa52000, paddr: 0x140a000)
ATTACH (pd: 27, ms: 34, rights: 0x7)
GRANT (pd: 27, obj: 34, rights: 0x7)
NEW MS (owner: 27, base: 0x16e00000, size: 0x83b000, flags 0x12, attr: 0x0) = 35
MAP (vaddr: 0x16e00000, size: 0x83b000, paddr: 0x16e00000)
ATTACH (pd: 27, ms: 35, rights: 0x5)
GRANT (pd: 27, obj: 35, rights: 0x5)
NEW MS (owner: 27, base: 0x1763b000, size: 0x577000, flags 0x12, attr: 0x0) = 36
MAP (vaddr: 0x1763b000, size: 0x577000, paddr: 0x1763b000)
ATTACH (pd: 27, ms: 36, rights: 0x6)
GRANT (pd: 27, obj: 36, rights: 0x6)
NEW MS (owner: 27, base: 0x17bb2000, size: 0x51000, flags 0x12, attr: 0x0) = 37
MAP (vaddr: 0x17bb2000, size: 0x51000, paddr: 0x17bb2000)
ATTACH (pd: 27, ms: 37, rights: 0x6)
GRANT (pd: 27, obj: 37, rights: 0x6)
EXPORT (thread: 28, obj: 7, local_key: 256, type: 3)
ATTACH (pd: 27, ms: 23, rights: 0x7)
GRANT (pd: 27, obj: 23, rights: 0x7)
EXPORT (thread: 28, obj: 23, local_key: 2000, type: 3)
ATTACH (pd: 27, ms: 24, rights: 0x7)
GRANT (pd: 27, obj: 24, rights: 0x7)
EXPORT (thread: 28, obj: 24, local_key: 2003, type: 3)
ATTACH (pd: 27, ms: 25, rights: 0x7)
GRANT (pd: 27, obj: 25, rights: 0x7)
EXPORT (thread: 28, obj: 25, local_key: 2004, type: 3)
ATTACH (pd: 27, ms: 26, rights: 0x7)
GRANT (pd: 27, obj: 26, rights: 0x7)
EXPORT (thread: 28, obj: 26, local_key: 2005, type: 3)
ATTACH (pd: 27, ms: 2, rights: 0x7)
GRANT (pd: 27, obj: 2, rights: 0x7)
EXPORT (thread: 28, obj: 2, local_key: 8, type: 3)
RUN THREAD (name: 28)
END
Total size: 0xbac bytes
```

This script is responsible for starting up four new
programs: [ig\_naming](ig_naming.md), [qdms](qdms.md), [quartz\_server](quartz_server.md) and
[AMSS](AMSS.md). The [ig\_naming](ig_naming.md) process is a standard iguana service
and its source is available in the public
OkL4 releases. The images for [ig\_naming](ig_naming.md), [qdms](qdms.md)
and [quartz\_server](quartz_server.md) are identical in all known radio
images but the image for [AMSS](AMSS.md) is different in
each.


## Building OkL4 ##
To build OkL4 you'll need to grab a cross compiler and
install python2.4 (yes, python2.4!). NICTA has
a prebuilt toolchain available which is suitable
(which has the same version of gcc reported in the KIP). You'll also
need the OkL4 source tree, I recommend using okl4\_release\_1.4.1.1.
Put the toolchain in your path, python2.4 before any other
python you have installed, and use the build tool to build:
```
PATH="`pwd`/../gcc-3.4.4-glibc-2.3.5/arm-linux/bin:/usr/local/bin:$PATH"
./tools/build.py machine=gumstix project=iguana wombat=True
```
All files will be generated under ./build.
To clean append "-c" or simply remove the ./build directory.
If you would like to see all the build steps, add
"VERBOSE\_STR=True" to the command line as well.

The version of genext2fs that ships in the tools subdirectory
is old and buggy and may crash on your machine.  If it does,
you can install a newer version in your PATH and edit
build/tools.py to use it:
```
    def Ext2FS(self, size, dev, env_name):
        #genext2fs = SConscript(os.path.join("linux", "tools", "genext2fs", "SConstruct"),
        #                       build_dir=os.path.join(self.builddir, "native", "tools", "genext2fs"),
        #                       duplicate=0)
        ramdisk = self.builddir + os.sep + "ext2ramdisk"
        cmd = self.Command(ramdisk, Dir(os.path.join(self.builddir,
                                                     "install")),
                           "genext2fs" + #genext2fs[0].abspath +
                           #" -b $EXT2FS_SIZE -d $SOURCE -f $EXT2FS_DEV $TARGET",
                           " -b $EXT2FS_SIZE -d $SOURCE -D $EXT2FS_DEV $TARGET -N 10000",
                           EXT2FS_SIZE=size, EXT2FS_DEV=dev)
```

You'll also have to replace linux/rootfs/dev.txt since
the file format has changed.  Replace it with the following lines

```
# name          type mode uid gid major minor start inc count
/dev            d    755  0    0    -    -    -    -    -
/dev/console    c    644  0    0    5    1    1    1    -
/dev/fd0        b    644  0    0    2    0    0    0    -
/dev/full       c    644  0    0    1    7    7    7    -
/dev/hda        b    644  0    0    3    0    0    0    -
/dev/hda        b    644  0    0    3    1    1    1    9
/dev/hdb        b    644  0    0    3    64   64   64   -
/dev/hdb        b    644  0    0    3    64   64   1    9
/dev/hdc        b    644  0    0    22   0    0    0    -
/dev/kmem       c    644  0    0    1    2    2    2    -
/dev/loop       b    644  0    0    7    0    0    1    4
/dev/mem        c    644  0    0    1    2    2    2    -
/dev/net        d    755  0    0    -    -    -    -    -
/dev/net/tun    c    644  0    0    10  200  200  200   -
/dev/null       c    644  0    0    1    3    3    3    -
/dev/pts        d    755  0    0    -    -    -    -    -
/dev/pts/       c    644  0    0   136   0    0    1    10
/dev/ptmx       c    644  0    0    5    2    2    2    -
/dev/ram        b    644  0    0    1    0    0    1    4
/dev/random     c    644  0    0    1    8    8    8    -
/dev/rtc        c    644  0    0    10  135  135  135   -
/dev/tty        c    644  0    0    5    0    0    0    -
/dev/tty        c    644  0    0    4    0    0    1    4
/dev/ttyS       c    644  0    0    4    64   64   1    4
/dev/urandom    c    444  0    0    1    9    9    9    -
/dev/zero       c    644  0    0    1    5    5    5    -
/dev/fb         c    644  0    0    29   0    0    0    -
/dev/fb         c    644  0    0    29   0    0    1    4
```

You can run the built programs using the skyeye simulator
at http://www.ertos.nicta.com.au/downloads/tools/skyeye-kenge-1.2.1n.tar.gz .
Unfortunately it has some problems with the files generated
by the Okl4 1.4.1.1 tree (I'm not sure why, it is the
simulator supported by the build process!).  I found that
sorting the elf sections in the resulting binary fixes
the issue. Use the provided http://code.google.com/p/docl4amss/source/browse/tools/sortelf.py
tool to sort the image before simulating it:
```
PATH="`pwd`/../gcc-3.4.4-glibc-2.3.5/arm-linux/bin:/usr/local/bin:$PATH"
./tools/build.py machine=gumstix project=iguana wombat=True
sortelf.py build/image.sim
skyeye -e build/image.sim -c tools/sim_config/gumstix.skyeye
```

### IDA signatures ###

A script for generating IDA signature files from the
compiled wombat code
is provided
and two signature files generated from the built binaries
are provided in the download section:
  * http://code.google.com/p/docl4amss/source/browse/tools/genSig
  * http://docl4amss.googlecode.com/files/iguana.sig
  * http://docl4amss.googlecode.com/files/iguana_server.sig


## References ##
  * NICTA releases
    * http://www.ertos.nicta.com.au/downloads/pistachio--devel--1.1--version-0.tar.gz - source and documentation
    * http://www.ertos.nicta.com.au/downloads/iguana-project--devel--1.1--version-0.tar.gz
    * http://ertos.nicta.com.au/software/prebuilt/ - prebuilt toolchains including http://www.ertos.nicta.com.au/downloads/tools/arm-linux-3.4.4.tar.gz
  * OKL4 releases
    * http://wiki.ok-labs.com/downloads/release-pre-2.0/Okl4_release_1.4.1.1.tar.gz
    * http://wiki.ok-labs.com/downloads/release-pre-2.0/Okl4_release_1.5.2.tar.gz
    * http://wiki.ok-labs.com/downloads/release-2.0.12/okl4_2.0.12.tar.gz
    * http://wiki.ok-labs.com/downloads/release-2.1/okl4_2.1.tar.gz
    * http://www.ok-labs.com/registrations/softwareDownload
  * Documentation
    * http://wiki.ok-labs.com/downloads/release-pre-2.0/Okl4-progmanual.pdf - OkL4 1.5.2 documentation
    * http://wiki.ok-labs.com/BuildOptions - build options