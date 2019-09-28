#!/usr/bin/env python3 

"""
./01.pca.py <plink.eigenvec>
"""

import sys 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA

vcf=pd.read_csv(sys.argv[1], sep = " ", header = None, index_col=0)
vcf= vcf.drop(columns=1)

# print(vcf)

n, p = vcf.shape

fig, ax = plt.subplots()
ax.scatter(vcf.iloc[:,0], vcf.iloc[:,1])

fig.savefig("pca.png")
plt.close(fig)