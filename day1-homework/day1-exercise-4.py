#!/usr/bin/env python 

import sys 

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f= sys.stdin


chromosome = []

for line in f:
    if line.startswith ("@"):
        continue 
    fields = line.split("\t")
    if fields[5] == "*":
        continue 
    if len(chromosome) < 10:
        chromosome.append(fields[2])
print (chromosome)
    