#!/usr/bin/env python3

"""
./01-clustering.py hema_data.txt
"""

import sys
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list

hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = 0)
df2=df.transpose()

link = linkage(df2, method='average', metric = 'euclidean')
leaf = leaves_list(link)

fig, ax = plt.subplots()
ax = dendrogram(link, truncate_mode = 'lastp', labels = df2.index, leaf_rotation = 90)
# ax = dendrogram(link, truncate_mode = 'lastp', leaf_rotation = 90)
plt.tight_layout()
fig.savefig("Dendrogram.png")
plt.close(fig)