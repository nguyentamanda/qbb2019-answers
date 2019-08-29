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
target_name_seq = {}
extended_things={}

for ident, sequence in target:
    sequence = sequence.upper()
    target_name_seq[ident]=sequence
    
    for i in range(0, len(sequence)-k+1):
        kmer=sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else: 
            target_dict[kmer]=[(ident, i)]

for ident, seq in query:
    seq = seq.upper()
    for j in range(0, len(seq)-k+1):
        kmers=seq[j:j+k]
        if kmers in target_dict:
            for j, ident in kmers[kmer]:
                sequ = target_name_seq[ident]
                lt= len(sequ) #length of the target
                lq=len(seq)#length of the query
                extend_right = True
                extended_kmer = kmer
            while True:
                if extend_right:
                    if sequence[j+k+1]==sequ[i+k+1]:
                        i+=1 
                        j+=1
                        extend_kmer += sequence[j+k+1]
                    else:
                        extend_right = False
                    else:
                        extended_things[ident]=[extended_kmer]
                        break
                if (i+k) == lt or (j+k) == lq:
                    extend_right = False
            #now gotta print it 
            
                    
                    
               # while querysequence[a] == querysequence[b]:
                    #kmers = kmer
                   # i + k + 1 targetstart
                   # j + k + 1 querystart
                   # target_name_seeq target sequence
                   # seq query sequence
                    
                    #for left extension, for an end, happend when the index of the target or the query is zero. for right extension, for end the length of either the the query or target 
                    #what 5 things do we need: kmer, i, j, target sequences, query sequences 
                    