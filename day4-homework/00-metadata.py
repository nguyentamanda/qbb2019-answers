#!/usr/bin/env python3 

"""
Create all.csv with FPKMs

Usage: .00-metadat.py <metadata.csv> <ctab_dir>
metadata = samples.csv
<ctab_dir> = ~/qbb2019/data/stringtie

we want it to look like:
t_name  gene_name   sample1, ..., sample n 
"""

import sys 
import os 
import pandas as pd

metadata=sys.argv[1]
ctab_dir=sys.argv[2]

fpkms={}


for i, line in enumerate(open(metadata)):
    if i == 0:
        continue 
    fields=line.strip("\n").split(",")
    srr_id=fields[0] #store the sample name
    stage = fields[1] + fields[2] #store the sex and stage 
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab") #we are print the path to each of the ctab files. we join the argv2, which is the path up until stringtie, adding the srrid from our samples file, then making sure that it ends with t_data.ctab
    # print(ctab_path)
    df = pd.read_csv(ctab_path, sep ="\t", index_col="t_name") #calling the ctab_paths we created in the thing 

#use the srr_id (SRR07893) as the columns
    fpkms["gene_name"]=df.loc[:,"gene_name"] #we want the gene names to be a column too
    fpkms[stage] = df.loc[:,"FPKM"] #make the FPKMs a column

df_fpkms=pd.DataFrame(fpkms) #make the dictionary into a dataframe

print(df_fpkms)
print(df_fpkms.describe) #get some cute summary stats for your dataframe

pd.DataFrame.to_csv(df_fpkms, "all.csv")
