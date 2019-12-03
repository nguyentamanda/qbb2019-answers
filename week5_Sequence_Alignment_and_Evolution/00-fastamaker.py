#!/usr/bin/env python3

"""
./00-fastamaker.py <blastn-results.tsv>
"""

import sys 

blastn=open(sys.argv[1])

for line in blastn:
    col=line.rstrip("\n").split("\t")
    print (">" + col[0])
    print (col[1])