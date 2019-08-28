#!/usr/bin/env python3


import sys 

f = open(sys.argv[1])
g = int(sys.argv[2])

gene_list=[]
for line in f: 
    column=line.rstrip("\n").split("\t")
    if column[0]=="3R" and column[2]=="gene" and 'gene_biotype "protein_coding"' in line:
        gene_start=int(column[3])
        gene_end=int(column[4])
        geneid=column[8]
        gene_list.append((gene_start, gene_end, geneid))
print (len(gene_list))

low=0 #keep track of what the new low is 
high=len(gene_list)-1 #keep track of what the new high is 
mid=0 #keep track of what the new middle is 
number_it=0 #number of iterations 

while (low <= high):
    mid = int((low+high)/2)
    number_it += 1
    if (high-low == 1):
        if (gene_list[low][0]-g)>(gene_list[high][1]):
            low=mid
        elif (gene_list[low][0]-g)<(gene_list[high][1]):
            high=mid
        else: 
            break
    if g < (gene_list[mid][0]): #pick low interval
        high=mid
    elif g > (gene_list[mid][1]): #pick the high interval
        low=mid
    else:
        break

print (gene_list[mid])
print(number_it)
    