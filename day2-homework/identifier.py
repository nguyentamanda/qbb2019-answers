#!/usr/bin/env python3

"""
identifier mapping 

./identifer.py <mapping file> <c_tab> <no match argument>
"""
import sys 

f = open(sys.argv[1])
g = open(sys.argv[2])

genes={}

for line in f:
    columns = line.rstrip("\n").split("\t")
    print(columns)
    flyid=columns[0]
    flyac=columns[1]
    genes[flyid]=flyac

for lne in g:
    cols=lne.rstrip("\n").split() #strips the newline character on the cols
    fly_ctab = cols[8]
    lnez=lne.rstrip("\n") #strips the newline characters on the lines
    if fly_ctab in genes:
        print(lnez, genes[fly_ctab],sep = "\t")
    elif fly_ctab not in genes and sys.argv[3] == "default":
        print(lnez, "default",sep="\t")
    elif fly_ctab not in genes and sys.argv[3] == "nothing":
        continue 
   
        