#!/usr/bin/env python3

"""Finds matching k-mers between a single query and a database of targets

usage: kmer_matcher.py <target.fa> <query.fa> <k>

./kmer_match_extender.py subset.fa droYak2_seq.fa 11 | less

if the 11bp of the query is found in the target, print the name of the sequence we found it in 
"""
import sys 
from fasta import FASTAReader

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k=int(sys.argv[3])

target_dict={} #stores the kmers from the target seq
target_name_seq = {} #connects the target sequence with the actual sequence
extended_things={}

for ident, sequence in target:
    sequence = sequence.upper()
    target_name_seq[ident]=sequence #stores the target sequences as values with their ident as the key
    
    for j in range(0, len(sequence)-k+1):
        kmer=sequence[j:j+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, j))
        else: 
            target_dict[kmer]=[(ident, j)]


###########

for ident, sequence in query: #sequence is the sequence of query
    sequence = sequence.upper() #uppercase the entire sequence 

    for i in range(0, len(sequence)-k+1): #i refers to the start of the sequence, subtracting k and adding 1 would move the kmer along to get different 11bp 
        kmer=sequence[i:i+k] #a new kmer is the sequence from the start of the sequence, i to the end, which is i+k (the length of the kmer), here i am using "i" to represent the start of the QUERY 
        
        if kmer in target_dict: #if the query kmer is in the dictionary of target kmers
            for ident, j in target_dict[kmer]: #just in case there are multiple things in for value, we use a dictionary to append to all, j is used to refer to the target start sequence
                
                target_seq = target_name_seq[ident] #target_seq is the sequence(s) of each ident, go into dictionary and take out target sequence 
                
                target_length = len(target_seq) #length of the target
                query_length = len(sequence) #length of the query
            
                extended_kmer = kmer #we will put our extended kmers here when they match 
                extend_right = True
                
                while extend_right == True: #while we are still extending right
                    if (j+k == target_length) or (i+k == query_length): #if the i or the j is equal to the length of either sequence, you have hit the end
                       # extended_things[ident] = extended_kmer #add that sequence to the dictionary because we have stoppped extension
                       if ident in extended_things:
                           extended_things[ident].append((extended_kmer, int(len(extended_kmer))))
                       else:
                           extended_things[ident]=[(extended_kmer, int(len(extended_kmer)))]
                       break #change extend_right to false so that it can stop extension
                       
                    if sequence[i+k] == target_seq[j+k]: #if the next nt from the qsequence matches that of the tsequence
                        extended_kmer += sequence[i+k] #add that nt to extended_kmer
                        i += 1 #add one to the query to move it along 
                        j += 1 #add one to the target to move it along
            
                    else: #if nothing else (meaning that we have no matches)
                       # extended_things[ident] = extended_kmer #add everything to the dictionary of extended things matched with their ident
                       if ident in extended_things:
                           extended_things[ident].append((extended_kmer, int(len(extended_kmer))))
                       else:
                           extended_things[ident]=[(extended_kmer, int(len(extended_kmer)))]
                       break
                    # print(ident, extended_kmer, len(extended_kmer))
 
# for ident in extended_things:
#     extended_things[ident].sort(key = lambda x:x[1])


# sorted_dict = sorted(list(extended_things.items()), key = lambda t:t[1][1])
for ident in extended_things:
    for extended_kmer in sorted(extended_things[ident], reverse = True, key = lambda t:t[1]):
        print (ident, extended_kmer)

# sorted_dict = sorted(extended_things.items(), key = lambda t:t[1])
# for ident, seq in sorted_dict:
#     for extended_kmer in seq:
#         print(ident, extended_kmer)

                    