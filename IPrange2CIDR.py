# script to convert IP ranges to CIDR notation
# version 1.0
# Author Bert de Jong
import ipaddress
import csv

# Read the csv file, set the delimiter and assign the values of the row to
# startip and endip. writes the result to a file. Includes dirty error handling
# to stdout.
file = input('Please input a filename: \n')
delim = input('Please enter the delimiter used in the csv file: \n')

with open(file, 'r') as csvfile, open('parse_ips.txt', 'w') as parsed:
    counter = 0
    errorcount = 0
    range = csv.reader(csvfile, delimiter=delim)
    for row in range:
        try:
            ip1 = row[0]
            startip = ipaddress.IPv4Address(ip1)
            ip2 = row[1]
            endip = ipaddress.IPv4Address(ip2)
            cidr = [ipaddr for ipaddr in
                    ipaddress.summarize_address_range(startip, endip)]
            for network in cidr:
                parsed.write(str(network))
                parsed.write('\n')
                counter += 1
        except ValueError:
            print('There was an error with this row:', row)
            errorcount += 1
            pass
print('Finished! File contains ' + str(counter) + ' networks.')
print('Encountered ' + str(errorcount) + ' errors. Please check standard '
                                         'output for errors.')




