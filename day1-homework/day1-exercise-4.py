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

#another way to do it
#you would still need to filter this so it counts the 10th alignment, this one would count the 10th line 
# for i. line in enumerate f:
#if i >= 10:
#break
#line = line.rstrip("\n")
#fields = line.split("\t")
#print(fields[2])