#!/usr/bin/env python3

import sys 

if len(sys.argv)>1:
    f= open(sys.argv[1])
    
else:
    f=sys.stdin

count = 0
for line in f:
    if line.startswith("@"):
        continue 
    fields = line.split("\t")
    if fields[5] == "*":
        continue 
    else:
        count += 1
print (count)
    