#!/usr/bin/env python3

"""
./02-Plot.py CTCF_ER4.bedtools.tools CTCF_G1E.bedtools.tools intersect.bed intersect2.bed
"""

import sys 
import matplotlib.pyplot as plt 
import numpy as np

er4 = open(sys.argv[1])
g1e = open(sys.argv[2])
# g1e = open(sys.argv[2])

er4_dict = {}
g1e_dict = {}

for line in er4: 
    col = line.rstrip("\n").split("\t")
    feat = col[3]
    if feat in er4_dict:
        er4_dict[feat] += 1
    else:
        er4_dict[feat] = 1

for line in g1e: 
    col = line.rstrip("\n").split("\t")
    feat = col[3]
    if feat in g1e_dict:
        g1e_dict[feat] += 1
    else:
        g1e_dict[feat] = 1

f3 = open(sys.argv[3])
f4 = open(sys.argv[4])

gained = 0
lost = 0

for line in f3:
    gained += 1

for line in f4:
    lost +=1
 
x_value = np.arange(len(er4_dict))
width = 0.3

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 10))
axes = axes.flatten()

axes[0].bar(x=["Lost", "Gained"], height = [lost, gained])
axes[0].set_xlabel("CTCF Binding Sites")
axes[0].set_ylabel("Number of Sites")

axes[1].bar(x=x_value - width/2, height = list(er4_dict.values()), width = width, color = "blue", label = "ER4")
axes[1].bar(x= x_value + width/2, height = list(g1e_dict.values()), width = width, color = "red", label = "G1E")
axes[1].set_xticks(x_value)
axes[1].set_xticklabels(er4_dict.keys())

axes[1].legend()
axes[1].set_xlabel("Features")
axes[1].set_ylabel("Number of Sites")

fig.suptitle("CTCF ChIP-Seq in Mice")


fig.savefig("bar.png")
plt.close(fig)