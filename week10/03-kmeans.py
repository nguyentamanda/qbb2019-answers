#!/usr/bin/env python3

"""
./03-kmeans.py hema_data.txt
"""

import sys
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
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
# print(centroids)

fig, ax = plt.subplots()
plt.scatter(df2['x'], df2['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

my_dict = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
print(my_dict)
    
# plt.show()
fig.savefig("kmeans.png")
plt.close(fig)