# L4 Analysis #

The Okl4 kernel used by the radio image is largely
standard but it has some non-standard extensions.

## misc system call ##
The misc syscall handler (sys\_arm\_misc in pistachio/arch/arm/src/exception.cc) has an
additional case for 0xe0 (ie. when SP has 0xffffffe0).
The handler for this call (at 0xF000E43C) switches on context->[r1](https://code.google.com/p/docl4amss/source/detail?r=1) for
the following cases:
1, 3,4,5,6,7,9,9,10,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30
34, 36, 40.
The case for [r1](https://code.google.com/p/docl4amss/source/detail?r=1)=22 is used by the quartz server.

XXX no analysis yet.

## XXX others ##
  * utcb reserved0 field is used for something
  * utcb platform\_reserved is used for something