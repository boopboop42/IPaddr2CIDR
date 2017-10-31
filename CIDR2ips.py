# This script converts a list with IPv4 networks in CIDR notation into a list
# containing the addresses in that network. Also prints out the nunmber of
# adresses in the list. Returns an iterator over the usable hosts in the
# network. The usable hosts are all the IP addresses that belong to the network,
# except the network address itself and the network broadcast address.
# version 1.0
# Author Bert de Jong


import ipaddress
counter = 0
errorcount = 0
with open('parse_ips.txt', 'r') as\
        network:
    try:
        for line in network:
            cidr = ipaddress.ip_network(line.strip())
            for addr in cidr.hosts():
                counter += 1
                print(addr)
    except ValueError:
        pass
print('Network(s) contain ' + str(counter) + ' adresses.')


