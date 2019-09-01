#!/usr/bin/env python3
"""
Usage: ./binary.py <gtf file> <number we are guessing> 
"""

import sys 

f = open(sys.argv[1]) #GTF file we want to use 
g = int(sys.argv[2]) #the number we are guessing, which, in this case is 21378950

#this part filters out all the protein coding genes
gene_list=[]
for line in f: 
    column=line.rstrip("\n").split("\t")
    if column[0]=="3R" and column[2]=="gene" and 'gene_biotype "protein_coding"' in line:
        gene_start=int(column[3])
        gene_end=int(column[4])
        geneid=column[8]
        gene_list.append((gene_start, gene_end, geneid)) #store the information of the gene list in a tuple that consists of the gene start, end, id
# print (len(gene_list))

low=0 #keep track of what the new low is
high=len(gene_list)-1 #keep track of what the new high is
mid=0 #keep track of what the new middle is
number_iterations=0 #number of iterations

while low <= high:
    mid = int((low+high)/2)
    number_iterations += 1 
    if (high-low == 1):
        break
        # if gene_list[low][1]-g > gene_list[high][0]-g:
        #     high = mid
        #     print (gene_list[mid])
        # elif gene_list[low][1]-g < gene_list[high][0]-g:
        #     low = mid
        #     print(gene_list[mid][0])
    if g < (gene_list[mid][0]): #pick the lower interval 
        high = mid 
    elif g > (gene_list[mid][1]): #pick the high interval 
        low = mid
    print (mid, low, high)

# print (gene_list[low]) #where to put the print statement?
# print(gene_list[high])
# print(gene_list[mid])

# print (abs(gene_list[low][1] - g))
# print(abs(gene_list[high][0]-g))

if (abs(gene_list[low][1] - g)) > (abs(gene_list[high][0]-g)):
    mid = high
    print(abs(gene_list[high][0]-g))
if (abs(gene_list[low][1] - g)) < (abs(gene_list[high][0]-g)):
    mid = low
    print (abs(gene_list[low][1] - g))

print(gene_list[mid])
print (number_iterations)

#answer
# gene: (21378977, 21381970, 'gene_id "FBgn0004110"; gene_version "1"; gene_name "tin"; gene_source "FlyBase"; gene_biotype "protein_coding";')
# 12
# number of iterations: 12
# number of basepairs away: 27


