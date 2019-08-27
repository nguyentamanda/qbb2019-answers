#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    f = open(sys.argv[1])

else:
    f=sys.stdin

count = 0
for line in f:
    line = line.rstrip("\n") #strip the return so that it reads just the reads with the NH:i:1 without the space afterwards
    fields = line.split("\t")
    for field in fields:
        if field == "NH:i:1":
            count += 1

print (count)