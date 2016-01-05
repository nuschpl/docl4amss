This project is for sharing information about the design and implementation of the L4/AMSS system in Qualcomm basebands. This information is reverse engineered from devices and is intended for use in security research and creating inter-operating software.

Work is currently centered around analyzing the baseband of
the HtcDream.


# Topics #

This page lists the major topics covered by the wiki.

  * SoftwareOverview
  * Phones
    * HtcDream
  * [Images](Images.md)
    * [CreatingImages](CreatingImages.md)
  * Baseband software components
    * OkL4 - small microkernel with kernel-mode functions
      * L4Analysis
    * [Iguana](Iguana.md) - some traditional operating system features
      * [IguanaNaming](IguanaNaming.md) server - a naming server
    * [Qdms](Qdms.md) server - a server for managing shared memory between clients and servers
    * [Quartz](Quartz.md) server
    * [Amss](Amss.md) server - qualcomm's baseband software
  * ReferencePage