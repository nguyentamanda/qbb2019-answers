#!/usr/bin/env python3

"""
velveth reads_2 21 -fastq reads_low_2.fastq
spades.py --only-assembler -o spades_reads12 -1 reads_low_1.fastq -2 reads_low_2.fastq 
lastz reference.fasta spades_reads12/K21/simplified_contigs.fasta --format=general --chain  >contigs_lz.csv

./03-dotplot.py <lastz file>
./03-dotplot.py contigs_spades_lastz_low.csv
"""

import sys 
import matplotlib.pyplot as plt
import pandas as pd

lastz = open(sys.argv[1])

start = []
end = []

for line in lastz: 
    if line.startswith("#"): 
        continue 
    cols = line.rstrip("/n").split("\t")
    for i in range(int(cols[5])-int(cols[4])):
        start.append(int(cols[9])+i)
        end.append(int(cols[4])+i)
        

# print(start)
# print (end)

# take the index of each thing, then plot it 
fig, ax = plt.subplots()
# ax.plot()
fig.suptitle("K21 Contigs Dotplot")

ax.scatter(x=start, y=end, alpha=0.4)
ax.set_xlabel("K21 Contigs Length (bp)")
ax.set_ylabel("Reference Length (bp)")

fig.savefig("contigs_lastz_velvet_better2.png")
plt.close(fig)
     
    
        
    