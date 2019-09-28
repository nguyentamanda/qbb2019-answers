#!/usr/bin/env python3

"""
./03-columnedit.py <phenotype data>
"""

import sys 
import pandas as pd

phenotype = open(sys.argv[1])

vcf=pd.read_csv(sys.argv[1], sep = "\t")
# vcf = vcf.drop(vcf.loc(1))
#
# print(vcf)

Family_ID = []
Sample_ID = []

for i, line in enumerate(phenotype): 
    if i == 0:
        continue
    cols = line.rstrip("\n").split("\t")
    col = cols[0].rstrip("\n").split("_")
    # print(col)
    Family_ID.append(col[0])
    Sample_ID.append(col[1])

#made a new data frame to add the family and sample ID to it, then took rewrote it as a df with just those two columns and concatenated it with the original df with the first column dropped.
phenotype = vcf.iloc[:,1:]

vcf['FID'] = Family_ID
vcf['IID'] = Sample_ID
vcf=vcf.loc[:,["FID", "IID"]]

df = pd.concat((vcf, phenotype), axis =1)

pd.DataFrame.to_csv(df, "clean.txt", sep="\t", index = False, na_rep= "NA")