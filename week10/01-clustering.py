#!/usr/bin/env python3

"""
./01-clustering.py hema_data.txt
"""

import sys
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list

hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = 0)

link = linkage(df, method='single', metric = 'euclidean')
leaf = leaves_list(link)

df3= df.transpose()
link2 = linkage(df3, method='single', metric = 'euclidean')
leaf2 = leaves_list(link2)

df4 = df.iloc[leaf,:]
df5 = df4.iloc[:, leaf2]

fig, ax = plt.subplots()

#Heat map
plt.pcolor(df4)
plt.yticks(np.arange(0.5, len(df5.index), 1), df5.index)
plt.xticks(np.arange(0.5, len(df5.columns), 1), df5.columns)

fig.savefig("HeatMap.png")
plt.close(fig)
