#!/usr/bin/env python3

"""
./01-Methylation.py SRR1035452_1_bismark_bt2_pe.bedGraph SRR1035454_1_bismark_bt2_pe.bedGraph
"""

import sys 

bedGraph1 = open(sys.argv[1])
bedGraph2 = open(sys.argv[2])

List1 = []
List2 = []

List1_uniq = []
List2_uniq = []

overlap = []

for i, line in enumerate(bedGraph1): 
    if i == 0: 
        continue 
    List1.append(line)
# print(List1)

for j, lines in enumerate(bedGraph2):
    if j == 0:
        continue 
    List2.append(lines)
# print(List2)

for item in List1:
    if item not in List2:
        List1_uniq.append(item)
    else:
         overlap.append(item)

for item in List2: 
    if item not in overlap:
        List2_uniq.append(item)
        
        
# print (len(List1))
# print (len(List2))
# print (len(List1_uniq))
# print (len(List2_uniq))
# print (len(overlap))

# for item in List1_uniq:
#     print (item)

for item in List2_uniq: 
    print(item)
    
    