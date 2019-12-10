#!/usr/bin/env python3 

"""
./01-plot.py memechip_out/fimo_out_1/fimo.tsv
"""

import sys
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats

motif = open(sys.argv[1])

mot_start = []

for i,line in enumerate(motif):
    if i == 0:
        continue
    if i > 140:
        continue
    cols = line.rstrip("\n").split("\t")
    start = cols[3]
    score = round(float(cols[6]))
    for j in range(score):
        mot_start.append(int(start))
    

mot_start.sort()

chr19 = [0]*61431566

for i in mot_start:
    for j in range(20):
        chr19[i+j] += 1
        
position = []
for i in range(len(chr19)):
    if chr19[i]!=0:
        for j in range(chr19[i]):
            position.append(i)


fig, ax = plt.subplots()
sns.distplot(position, hist= True, rug = True, kde = True)
ax.set_xlim(0,61431566)

x_string_labels = ['0','10000000','20000000','30000000','40000000','500000000','60000000','70000000']
ax.set_xticklabels(x_string_labels)
fig.autofmt_xdate()


ax.set_ylabel("Frequency")
ax.set_xlabel("Position")
fig.tight_layout()
fig.savefig("plot.png")
plt.close(fig)