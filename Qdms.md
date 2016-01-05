# QDMS #

The Qdms server provides a number of RPCs for managing
shared-memory communications between processes and servers.
This component is not open sourced but it uses many
of the same open source libraries as IguanaNaming server uses.

XXX more details on how its used.

# Analysis #

The IDL served by QDMS is documented in http://code.google.com/p/docl4amss/source/browse/analysis/qdms/idl.txt

An IDC file (for IDA Pro) is provided that adds names for
many of the functions used in the process: http://code.google.com/p/docl4amss/source/browse/analysis/qdms/qdms.idc

XXX I have not yet analyzed any programs making use of QDMS.
It appears to set up a bunch of shared memory regions between
servers and clients and place some data structures in those
regions.  Its probably got ring buffers for both directions of
communication....