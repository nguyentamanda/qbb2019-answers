#!/usr/bin/env python3

"""
Boxplot all transcripts for a given gene 

usage: ./01-boxplot.py <gene_name> <fpkms.csv> 

our fpkms.csv is all.csv 

all.csv is already in a dataframe
"""

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name") #index columns are for labels, each one has to be unique 
# print(df)

goi = df.loc[:,"gene_name"] == gene_name #filter for the transcripts that belong to the gene we indicated in the command line we did this using boolean filtering. 

fpkms = df.drop(columns = "gene_name") #drop removed the column "gene_name" we added in the last code because we used it to filter the genes we want, now we dont need it anymore

# print(fpkms.loc[goi,:])

females = []
males = []

for col in fpkms.columns:
    if "f" in col:
        females.append(True)
    else: 
        females.append(False)

for colum in fpkms.columns:
    if "f" not in colum:
        males.append(True)
    else:
        males.append(False)

fig, ax = plt.subplots(2)

f = np.log2(fpkms.loc[goi,females]+0.001)
ax[0].boxplot(f.T)
ax[0].set_title("Females")

m = np.log2(fpkms.loc[goi,males]+0.001)
ax[1].boxplot(m.T)
ax[1].set_title("Males")

fig.savefig("boxplot.png")
plt.close(fig)