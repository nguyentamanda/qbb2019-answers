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

# class FASTAReader(object):
#     def __init__(self, fh):
#         self.fh = fh
#         self.last_ident = None
#         self.eof=False #eof = end of file
#     def next(self):
#         if self.eof: #if we have reached the end of the file
#             return None, None
#         elif self.last_ident is None: #tells us we are on the first line
#             line = self.fh.readline()
#             assert line.startswith(">"), "Not a FASTA file"
#             ident = line[1:].rstrip("\n")
#         else:
#             ident = self.last_ident
#     #if we reached this point, ident is set correctly
#         sequences = []
#         while True:
#             line = self.fh.readline()
#             if line == "":
#                 self.eof = True
#                 break
#             elif line.startswith(">"):
#                 self.last_ident = line[1:].rstrip("\n")
#                 break
#             else:
#                 sequences.append(line.strip())
#         sequence = "".join(sequences)
#         return ident, sequence

# reader=FASTAReader(contigs)

start = []
end = []

for line in lastz: 
    if "#" in line: 
        continue 
    cols = line.rstrip("/n").split()
    if cols[7] != "-":
        start.append((int(cols[5])-int(cols[4])))
        end.append(int(cols[8]))

# print(start)
# print (end)

# take the index of each thing, then plot it 
fig, ax = plt.subplots()
ax.plot()
fig.suptitle("K21 Contigs Dotplot")
ax.scatter(x=start, y=end, alpha=0.4)
ax.set_xlabel("K21 Contigs Length (bp)")
ax.set_ylabel("Reference Length (bp)")

fig.savefig("contigs_lastz_velvet_better.png")
plt.close(fig)
     
    
        
    