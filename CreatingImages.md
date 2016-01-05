# Creating Images #

There are many available radio images.  The [Images](Images.md) page
lists and compares them.  As can be seen, most of the sections
of the elf file in the radio images are identical or nearly so across all
version. The AMSS component is the primary part of the elf file
that changes from version to version.

Our analysis focuses primarily on the ota-radio-2\_22\_19\_26I
radio image.  This image can be found at
http://code.google.com/p/android-roms/wiki/Radio_Update
among other places. The file has an image for a flash
filesystem but we're primarily interested in the ELF
file that has the L4 kernel, Iguana subsystem and related
servers and the AMSS software.  A script is provided to
extract the ELF file and split it into a number of smaller
ELF files:

http://code.google.com/p/docl4amss/source/browse/tools/getPrograms.py

After running this program on the radio.img file the program
will write out a number of files:
  * elf - the ELF file with the L4 kernel, Iguana and AMSS
  * l4 - the [OkL4](OkL4.md) kernel
  * iguana - sections of the ELF file containing the [Iguana](Iguana.md) server
  * ig\_naming - sections for the IguanaNaming server
  * quartz - sections for the [Quartz](Quartz.md) server
  * qdms - sections for the [Qdms](Qdms.md) server
  * amss - sections for the [Amss](Amss.md) server