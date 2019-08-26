#!/usr/bin/env python3

import sys 

if len(sys.argv)>1:
    f= open(sys.argv[1])
    
else:
    f=sys.stdin

count = 0
for line in f:
    count += 1
print (count)
    