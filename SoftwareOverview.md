# Introduction #

The baseband software in the HTC Dream is made
up of several components.  At the lowest layer there
is the OkL4 kernel. This is a small microkernel that
provides the supervisor-mode part of the operating
system.  Several user-mode programs run on top of
this kernel. They all share a single address space
although they do have memory protection between
several "protection domains".

The most important
program is the [Iguana](Iguana.md) server which performs many
operating system services on behalf of client programs.
This is the only program allowed to make several important
OkL4 system calls to control memory mapping, create
protection domains and create threads.  The [Iguana](Iguana.md)
server receives requests through the L4 IPC mechanism.

Several other servers are also present to provide services.
These include the IgNaming service, which is used to
bind names to objects and look up objects by name, and
the [Qdms](Qdms.md) service which is used to manage shared memory
for interprocess communication.  There is also a Quartz
service which provides some more naming and IPC services
(XXX need to better understand quartz's role).  These
services make use of [Iguana](Iguana.md) and communicate with clients
via L4 IPC.

Finally there is the main [Amss](Amss.md) process.  This process
is the largest and contains many individual subsystems
such as the GSM system.  At the lowest layers are some
operating system services that provide an emulation
layer of an older OS called [REX](REX.md).  (XXX need to build
a more complete picture of how REX is built on L4/Iguana,
the various "CS" features,  how communication happens
between AMSS processes, what various subcomponents are
started up, etc).


![http://docl4amss.googlecode.com/files/amssArch.png](http://docl4amss.googlecode.com/files/amssArch.png)

The processes communicate via L4 IPC.

![http://docl4amss.googlecode.com/files/amssArch2.png](http://docl4amss.googlecode.com/files/amssArch2.png)