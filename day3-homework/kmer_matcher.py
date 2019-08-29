#!/usr/bin/env python3

"""Finds matching k-mers between a single query and a database of targets

usage: kmer_matcher.py <target.fa> <query.fa> <k>

if the 11bp of the query is found in the target, print the name of the sequence we found it in 
"""
import sys 
from fasta import FASTAReader

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k=int(sys.argv[3])

target_dict={}

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k+1):
        kmer=sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else: 
            target_dict[kmer]=[(ident, i)]

for ident, seq in query:
    seq = seq.upper()
    for i in range(0, len(seq)-k+1):
        kmers=seq[i:i+k]
        if kmers in target_dict:
            for ident, j in target_dict[kmer]:
                print(ident, j, i, kmer)