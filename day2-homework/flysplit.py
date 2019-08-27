#!/usr/bin/env python3
"""
Parses the FlyBase genes files to include only the geneIDs and UNiProtIDs

usage: ./flysplit.py <gene file name>
"""

import sys 

f=open(sys.argv[1])

for i, line in enumerate(f):
    if "DROME" not in line:
        continue 
    column= line.split()
    if "FBgn" not in column[-1]:
        continue
    flyac=column[-2] #-1 is the last column, and -2 is the second to last column
    flyid=column[-1]
    print (flyid,'\t',flyac)