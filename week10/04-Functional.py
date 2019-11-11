#!/usr/bin/env python3

"""
./04-Functional.py hema_data.txt Adcy6
"""

import sys
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
import scipy.stats as sp
from sklearn.cluster import KMeans

hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = "gene", header = 0)

cfu = df["CFU"].values 
poly = df["poly"].values

Data = {'x': cfu, 
        'y': poly
        }
# print(Data)

df2 = pd.DataFrame(Data, columns=['x','y'])
# print(df2)

kmeans = KMeans(n_clusters=5).fit(df2)
centroids = kmeans.cluster_centers_

labels = list(kmeans.labels_)
genes = list(df.index.values)

goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]

related_genes=[]

for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)
        
for gene in related_genes:
    print(gene)