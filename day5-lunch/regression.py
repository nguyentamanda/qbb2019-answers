#!/usr/bin/env python3

"""
Usage ./regression.py <fpkms> <histone1> <histone2> <histone3>

fpkms = all file 

./regression.py ../results/stringtie/SRR072893/t_data.ctab H3K4me1.tab H3K4me3.tab H3K9me3.tab 
"""

import sys 
import numpy as np 
import pandas as pd 
import statsmodels.api as sm 

fpkm = sys.argv[1]
his1 = sys.argv[2]
his2 = sys.argv[3]
his3 = sys.argv[4]

fpkm_df = pd.read_csv(fpkm, sep="\t", index_col ="t_name")
his1_df = pd.read_csv(his1, sep="\t", index_col=0, header= None) #these files dont have a header
his2_df = pd.read_csv(his2, sep="\t", index_col=0, header= None)
his3_df = pd.read_csv(his3, sep="\t", index_col=0, header= None)

hist_dict={"FPKM": fpkm_df.loc[:,"FPKM"], 
            "H1": his1_df.iloc[:,-1],
            "H2": his2_df.iloc[:,-1], 
            "H3": his3_df.iloc[:,-1]}

histone_df = pd.DataFrame(hist_dict )

model = sm.formula.ols(formula = "FPKM ~ H1 + H2 + H3", data=histone_df)
ols_result = model.fit()
print(ols_result.summary())