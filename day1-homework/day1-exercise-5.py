#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

mapq = []
for line in f:
    if line.startswith ("@"):
        continue 
    fields=line.split("\t")
    if fields[5]== "*":
        continue 
    mapq.append(int(fields[4]))

summap = sum(mapq)
length = len(mapq)

avger = summap / length

print (avger)