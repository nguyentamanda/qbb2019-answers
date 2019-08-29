#!/usr/bin/env python3

"""
usage: 01-hist.py <ctab> <mu> <sigma> <skewness> 3 2.3 1

Make a histogram 
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue 
    fields=line.rstrip("\n").split("\t")
    if float(fields[11])>0:
        fpkms.append(float(fields[11]))

fig, ax = plt.subplots()

my_data=np.log2(fpkms) 
ax.hist(my_data, bins = 100, density = True)

mu = float(sys.argv[2]) #average
sigma = float(sys.argv[3]) #stdev
a = float(sys.argv[4]) #skewness parameter

x = np.linspace(-15, 15, 100) 
y = stats.skewnorm.pdf(x, a, mu, sigma)
ax.plot(x, y, label="a=1, mu=3, sig=2.3")

y_norm = stats.norm.pdf(x, mu, sigma)
ax.plot(x, y_norm, label="normal dist")

ax.legend()

plt.title("FPKM distribution")
plt.xlabel("log2 FPKMs")
plt.ylabel("log2 Frequency")

fig.savefig("fpkms.png")
plt.close(fig)