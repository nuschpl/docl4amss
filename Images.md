# Images #

There are many different radio images for the HtcDream.
Here are the images that I was able to find, indexed by
the MD5 sum of the radio.img file:

  * [4e04b3cf8db5356536519691fc1b75e3](4e04b3cf8db5356536519691fc1b75e3.md) - "original", origin unknown.
  * [d3a7a9c292e8643b4c23568349ae2bb4](d3a7a9c292e8643b4c23568349ae2bb4.md) - from Radio\_Dream\_RC33\_1\_22\_14\_11.zip. This is similar to the "original" image.
  * [623721055105bcef43735298dd5138cb](623721055105bcef43735298dd5138cb.md) - from ota-radio-2\_22\_19\_26I.zip This is currently the main image I am analyzing.
  * [76ceb8d991c8f25220dcdbf33fa79f45](76ceb8d991c8f25220dcdbf33fa79f45.md) - from Radio\_Sapphire\_2\_22\_19\_23.zip. This is similar to the ota-radio-2\_22\_19\_26I image
  * [d800642198456993467c675796c67aed](d800642198456993467c675796c67aed.md) - from G1-radio-2\_22\_23\_02.zip
  * [0eb7c5530ef38eeaa07590e6924c7814](0eb7c5530ef38eeaa07590e6924c7814.md) - radio-3.22.26.17\_dream.img


The images do not vary that much and all seem to share
a common L4 kernel image (although some with different
configuration options in the data segment).

The following
table compares several of the ELF segments that are
aligned at the same virtual address. Each letter in the versions column
represents one of the images, letters placed together indicate
the same version and versions listed separately indicate
different versions.

|  **VirtAddr**   | **Flg** | **Descr**       | **different versions** |
|:----------------|:--------|:----------------|:-----------------------|
|  0xf0000000     | RWE     | L4 and libs       | rdosg3                 |
|  0xf0020000     | RW      | L4 data           | rd, os, g, 3           |
|  0xb0000000     | R E     | iguana rootserver | rdosg3                 |
|  0xb0040000     | RW      | iguana data       | rdosg3                 |
|  0xb0d00000     | RW      | bootinfo          | rd, os, g, 3           |
|  0xb0e00000     | RW      | ?                 | rdosg3                 |
|  0xb0100000     | R E     | ig\_naming server  | rdosg3                 |
|  0xb0140000     | RW      | ig\_naming data    | rdosg3                 |
|  0xb0200000     | R E     | qdms server       | rdosg3                 |
|  0xb0240000     | RW      | qdms data         | rdosg3                 |
|  0xb0300000     | RWE     | quartz server     | rdosg3                 |
|  0x00b07000     | R E     | amss server       | r, d, o, s, g, 3       |
|  0x00b0a000     | R E     | more amss         | r, d, o, s, g, 3       |
|  0x16e00000     | R E     | more amss...      | r, d, o, s, g, 3       |


| **Image** | **Key**                   | **Image** | **Key** |
|:----------|:--------------------------|:----------|:--------|
| orig      | r                         | ota-radio-2\_22\_19\_26I | o       |
| Radio\_Dream\_RC33\_1\_22\_14\_11 | d                         | Radio\_Sapphire\_2\_22\_19\_23 | s       |
| G1-radio-2\_22\_23\_02 | g                         | radio-3.22.26.17\_dream  | 3       |


# Creating images #

The CreatingImages page contains information for extracting
programs from the radio image for analysis.



# References #
  * http://code.google.com/p/android-roms/wiki/Radio_Update - has several radio images available for download
  * http://www.mediafire.com/?zgnzmex2mrj - G1-radio-2\_22\_23\_02 image
  * http://briancrook.ca/android/rogers/dream_update/radio-3.22.26.17_dream.img - radio-3.22.26\_17\_dream image