#!/usr/bin/env python3

"""
velveth velvet_reads_12 21 -fastq reads_low_1.fastq reads_low_2.fastq 
velvetg velvet_reads_12/
lastz reference.fasta velvet_reads_12/contigs.fa --format=general --chain > contigs_velvet_lastz_low.csv

spades.py --only-assembler -o spades_reads12 -1 reads_low_1.fastq -2 reads_low_2.fastq 
lastz reference.fasta spades_reads12/K21/simplified_contigs.fasta --format=general --chain  >contigs_spades_lastz_low.csv
 
./02-contigs.py <contigs file>
"""

import sys 
import matplotlib.pyplot as plt
import pandas as pd

contigs = open(sys.argv[1])

class FASTAReader(object):
    def __init__(self, fh): 
        self.fh = fh
        self.last_ident = None
        self.eof=False #eof = end of file 
    def next(self):
        if self.eof: #if we have reached the end of the file
            return None, None 
        elif self.last_ident is None: #tells us we are on the first line
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file" 
            ident = line[1:].rstrip("\n") 
        else: 
            ident = self.last_ident
    #if we reached this point, ident is set correctly
        sequences = []
        while True: 
            line = self.fh.readline()
            if line == "":
                self.eof = True 
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n") 
                break
            else: 
                sequences.append(line.strip())
        sequence = "".join(sequences)
        return ident, sequence

reader=FASTAReader(contigs)

contigs= []
while True:
    ident, sequence = reader.next()
    if ident is None:
        break
    # print(ident, sequence, sep = "\t")
    contigs.append(sequence)

print("Number of contigs =", len(contigs))

sorted_contigs=sorted(contigs, key=len, reverse = True)
# print(sorted_contigs)

print("Max length =", len(sorted_contigs[0]))
print("Min length =", len(sorted_contigs[-1]))

total = 0
for i in contigs: 
    total+=len(i)

average = total/len(contigs)
print("Average length=", average)
    
acc = 0
for i in range(len(sorted_contigs)): 
    acc += len(sorted_contigs[i])
    if acc >= total/2:
        print("N50 = ", len(sorted_contigs[i]))
        break