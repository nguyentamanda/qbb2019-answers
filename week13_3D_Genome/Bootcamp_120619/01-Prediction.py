#!/usr/bin/env python2

"""
./01-Prediction.py chr10_activity_binned.bed chr10_rna_binned.bed 
"""

import hifive
import numpy
import sys 

bed1 = open(sys.argv[1])
bed2 = open(sys.argv[2])

act = {}
rna = {}

for i, line in enumerate(bed1):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = ((int(col[1]) - 5000000) / 5000)
        act[index]= col[4]

for i, line in enumerate(bed2):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[1]) - 5000000) / 5000
        rna[index]= col[4]

hic = hifive.HiC('PROJECT_NAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

int_act = {}

for key1 in rna:
    total_act = 0
    for key2 in act:
        total_act+=float(act[key2])*data[key1][key2]
    int_act[key1] = total_act

rna_list = []
int_list = []

for index in rna:
    rna_list.append(float(rna[index]))
    int_list.append(int_act[index])
rna_array = numpy.array(rna_list)
int_array = numpy.array(int_list)

rval = numpy.corrcoef(rna_array, int_array)[0,1]
print rval

# for key in rna:
#     print key, int_act[key]
