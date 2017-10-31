# IPconversionTools
Some scripts to convert lists of networks and IP's.

IPrange2CIDR:
Converts a csv file with start and endip to a list with networks in CIDR format. Just start the script, point to the file 
and choose the delimiter used in the csv. This results in a file called parse_ips.txt containing the list of networks. Also prints out rows
that contain errors, like a smaller endip after a startip. 

CIDR2ips:
Takes the output from the previous script to a list of usable hosts. It scipts the network (e.g. 192.168.1.0) and the broadcast addres. 
