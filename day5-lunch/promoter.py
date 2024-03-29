#!/usr/bin/env python3

"""
Usage: ./promoter.py <c_tab_path> 
"""

import sys 
import pandas as pd 


df=pd.read_csv(open(sys.argv[1]), sep="\t")

genes = df.loc[:,(("t_name","start", "end", "chr", "strand"))]

for i, t in genes.iterrows(): 
    if t.loc["strand"] == "+":
        prota = int(t.loc["start"]) + 500
        protb = int(t.loc["start"]) - 500
        a = t.loc["chr"]
        t_name = t.loc["t_name"]
        
        if protb > 0: 
            print(a, protb, prota, t_name, sep = "\t")
        else:
            print(a, t.loc["start"], prota, t_name, sep = "\t")
    
    elif t.loc["strand"]=="-":
        protc = int(t.loc["end"])+500
        protd = int(t.loc["end"])-500
        a = t.loc["chr"]
        t_name = t.loc["t_name"]
    
        if protd > 0: 
            print(a, protd, protc, t_name, sep = "\t")
        else:
            print(a, t.loc["start"], protc, t_name, sep = "\t")

