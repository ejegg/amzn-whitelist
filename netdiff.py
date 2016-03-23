#! /usr/bin/env python
# Calculates the disjunction of two sets of IP ranges
from sys import argv
from netaddr import IPSet

if len(argv) != 3:
    print('Usage: {0} include.txt exclude.txt'.format(argv[0]))
    exit()

net = IPSet()
incfile = open(argv[1])
for line in incfile:
    net = net | IPSet([line])
exfile = open(argv[2])
for line in exfile:
    net.remove(line)
for cidr in net.iter_cidrs():
    print(cidr)
