#!/usr/bin/env python3

""""
Make a scatterplot that plot the FRKM values of two samples

usage: ./scatter.py <ctab1> <ctab2>
"""

import sys 
import pandas as pd 
import os
import matplotlib.pyplot as plt
import numpy as np

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2=sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm={name1 : ctab1.loc[:,"FPKM"], 
      name2 : ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)

fig, ax = plt.subplots()
# print(np.log2(df.loc[:,name1]))
ax.scatter(np.log2( df.loc[:,name1]+0.001), np.log2(df.loc[:,name2]+0.001), alpha = 0.1)

np.polyfit(np.log2( df.loc[:,name1]+0.001), np.log2(df.loc[:,name2]+0.001), deg = 1)

plt.title("FPKM1 vs FPKM2")
plt.xlabel("log2 FPKM1")
plt.ylabel("log2 FPKM2")

fig.savefig("scatter.png")
plt.close(fig)

#print(df)
#print(type(df))