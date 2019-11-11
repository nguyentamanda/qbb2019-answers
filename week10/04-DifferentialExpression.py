#!/usr/bin/env python3

"""
./04-DifferentialExpression.py hema_data.txt
"""

import sys
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
import scipy.stats as sp

hema = open(sys.argv[1])

df = pd.read_csv(hema, sep = "\t", index_col = 0)

diff_exp_high = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2)) >=2
diff_exp_low = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2)) <= 0.5

diff_exp_genes = df[diff_exp_high | diff_exp_low] #it prints out a whole dataframe, we just got the genes that have 2fold exp, we will now test

for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    # print(gene_name,sp.ttest_rel(sample1, sample2).pvalue)
    if sp.ttest_rel(sample1, sample2).pvalue <= 0.05:
        print(gene_name,sp.ttest_rel(sample1, sample2).pvalue)
    
# for gene, row in diff_exp_genes.iterrows():
#     diff_high = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2))
#     diff_low = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2))
#