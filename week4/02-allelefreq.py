#!/usr/bin/env python3

"""
02-allelefreq.py <vcf file>
"""

import sys 
import matplotlib.pyplot as plt 
import pandas as pd

vcf = open(sys.argv[1])

maf = []

for line in vcf: 
    if "CHR" in line:
        continue
    cols = line.rstrip("\n").split()
    values = float(cols[4])
    maf.append(values)

fig, ax = plt.subplots()
ax.hist(maf, bins = 100, density = True)

plt.tight_layout()
fig.savefig("allelefeq.png")
plt.close(fig)