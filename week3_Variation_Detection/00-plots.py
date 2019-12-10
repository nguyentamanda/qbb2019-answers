#!/usr/bin/env python3

"""
./00-plots.py A01_filter_snpEff.vcf
"""

import sys 
import matplotlib.pyplot as plt
import numpy as np

vcf = open(sys.argv[1])

read_depth = []

quality=[]

freq = []

effect = {}

for line in vcf: 
    if line.startswith("#"):
        continue 
    cols= line.rstrip("\n").split("\t")
    fields = cols[7].rstrip("\n").split(";")
#Read Depth    
    dp = fields[7].rstrip("\n").split("=")
    read_depth.append(dp[1])
#Genotype Quality 
    quality.append(int(float(cols[5])))
#Allele Frequency 
    af = fields[3].rstrip("\n").split("=")
    freq.append(af[1])
#Summary of Predicted Effects    
    cola = fields[41].rstrip("\n").split("|")
    ai = cola[1]
    if ai in effect: 
        effect[ai] += 1
    else: 
        effect[ai] = 1

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

#Read Depth Histogram
ax1.hist(read_depth, bins = 100, density = True)
ax1.set_title("Read Depth Distribution", size = 15)
ax1.set_xlabel("Read Depth")
for tick in ax1.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(5)

#Quality Histogram
ax2.hist(quality, bins = 50, density = True, range = (0, 2500))
ax2.set_title("Quality Distribution", size = 15)
ax2.set_xlabel("Quality", size = 10)

#Allele Frequency Histogram
ax3.hist(freq, bins = 50, density = True)
ax3.set_title("Allele Frequency Histogram", size = 15)
ax3.set_xlabel("Frequency", size = 10)
for tick in ax3.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(8)


#Summary of Predicted Effects
plt.bar(range(len(effect)), list(effect.values()), align = 'center')
plt.xticks(range(len(effect)), list(effect.keys()), rotation = 'vertical', size = 8)
ax4.set_title("Predicted Effects", size = 15)
ax4.set_xlabel("Effects", size = 10)
ax4.set_ylabel("Frequency", size = 10)

fig.set_size_inches(40, 14)
plt.tight_layout()
fig.savefig("plots.png")
plt.close(fig)
