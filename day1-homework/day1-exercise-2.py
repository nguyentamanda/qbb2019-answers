#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f=sys.stdin

count = 0
for line in f:
    fields = line.split("\t")
    for field in fields:
        if field == "NM:i:0":
            count += 1
print (count)