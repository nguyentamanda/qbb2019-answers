#!/usr/bin/env python3

"""
./02-nucleotides.py 2-mafft.parsed.tsv 2-blastn-results.tsv
"""

import sys

mafft = open(sys.argv[1])
blastn = open(sys.argv[2])

protein_dict = {}
sequence_dict = {}
back_to_nucleo = {}

codon_table = {
"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V", 
"TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V", 
"TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V", 
"TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V", 
"TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
"TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", 
"TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", 
"TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", 
"TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D", 
"TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
"TAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", 
"TAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E", 
"TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G", 
"TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", 
"TGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
"TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
}

#load the protein dictionary
for line in mafft: 
    col = line.rstrip("/n").split(" ")
    cols = col[0].rstrip("\n").split(".")
    idz = cols[0]
    seq = col[1]
    protein_dict[idz] = seq

# print (protein_dict)

#load the nucleotide sequence dictionary 
for line in blastn:
    col = line.rstrip("\n").split("\t")
    cols = col[0].rstrip("\n").split("|")
    colz = cols[3].rstrip("\n").split(".")
    idz = colz[0]
    seq = col[1]
    sequence_dict[idz] = seq
# print(sequence_dict)

#back to nucleotides     
for idz in protein_dict:
    back_to_nuc= ""
    nuc_pos = 0
    protein_seq = protein_dict[idz]
    sequence_seq = sequence_dict[idz]

    for char in protein_seq:
        if char == "-": # '-' means that there is a gap
            back_to_nuc += "---"

        else:
            codon = sequence_dict[idz]
            back_to_nuc += sequence_seq[nuc_pos:nuc_pos+3]
            nuc_pos += 3
    back_to_nucleo[idz]=back_to_nuc
# print(back_to_nucleo)

#count the dS and dN mutations
length_of_query = len(sequence_dict["query"])

# dS_dict = {}
# dN_dict = {}

for i in range(0, length_of_query, 3):
    query_codon = sequence_dict["query"][i:i+3]
    dS = 0
    dN = 0
    for seq_id in sequence_dict:
        if seq_id == "query":
            continue 
        seq_codon = sequence_dict[seq_id][i:i+3]
        if seq_codon not in codon_table:
            continue
        if seq_codon != query_codon:
            if codon_table[seq_codon] == codon_table[query_codon]:
                dS += 1
            else:
                dN += 1
    print ("Codon:"+ seq_codon, "dS:" + str(dS), "dN:" + str(dN))