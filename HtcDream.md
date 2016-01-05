# Introduction #

This page discusses the HTC Dream phone, also called
the Android Developer Phone 1 (ADP1) and the T-mobile G1.

# JTAG #
XXX this section is still in progress.XXX

The HtcDream has JTAG contacts on its main board.
There are a few suppliers that sell contact boards
for connecting to these pins without any soldering:
  * http://www.ipmart.com/main/product/JTAG,Adapter,compatible,for,HTC,Dream,,Google,G1,277854.php?prod=277854
  * http://www.gsm-technology.com/index.php/en_US,details,id_pr,7183,menu_mode,categories.html

or you can solder the contacts directly.  The contact
points are shown here:

![http://docl4amss.googlecode.com/files/G1_JTAG_signals.jpg](http://docl4amss.googlecode.com/files/G1_JTAG_signals.jpg)

and here is a picture of someone who has soldered
the contacts:

![http://docl4amss.googlecode.com/files/soldered.jpg](http://docl4amss.googlecode.com/files/soldered.jpg)

If you use a contact board you will not be able to
connect the two connectors that are next to the
contact points while using JTAG.  You should
leave the master connection (from the south side
of the board) connected but do not need to leave
the camera (left) or ascii-keyboard (right) connectors
connected.

You'll also need to power your board
with an external supply.
The HtcDream will not power up without a battery
in place even while connected to a USB port and
there is no room to physically connect the battery
while using a contact board.
XXX I need to investigate
details on power more. (The battery connector has
three terminals and you cannot simply provide power
to two of them.  I tried masking off terminals on
the battery one at a time).

The following video shows one of the contact boards in operation.
As you can see they have the south connector in place but
do not have any other connectors attached to the main board.

http://www.youtube.com/watch?v=eITMEEF_AIc



The contact boards are pretty poorly documented.  Here are
pictures of the board I am using:

![http://docl4amss.googlecode.com/files/contact.jpg](http://docl4amss.googlecode.com/files/contact.jpg)

![http://docl4amss.googlecode.com/files/G1_Dream_485.jpg](http://docl4amss.googlecode.com/files/G1_Dream_485.jpg)

There is a small circle next to pin 1 of the JTAG connector.
There are also two pins on the upper right of the top board
for power (XXX need more investigation here).

## References ##
  * http://mikechannon.net/PDF%20Manuals/HTC%20Dream%20SM%20(A04).pdf - service manual describing how to disassemble the HtcDream