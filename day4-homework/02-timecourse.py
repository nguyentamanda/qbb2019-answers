#!/usr/bin/env python3

""""
Create a time course of a given transript of females 

Usage: ./02-timecourse.py <samples.csv> <FPKMs> <replicates> <ctab_dir> <

./02-timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv ~/qbb2019/data/replicates.csv ~/qbb2019-answers/results/stringtie

"""
import sys 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import os

#Specify transcript of interest 
t_name=sys.argv[1]
samples=pd.read_csv(sys.argv[2]) #load in the meta data 
fpkm_file=sys.argv[3]
replicates=sys.argv[4]
ctab_data_dir=sys.argv[5]

def sort_sex(sex):
    soi = samples.loc[:,"sex"] == sex
    stages = samples.loc[soi, "stage"]
    fpkms = pd.read_csv(sys.argv[3], index_col="t_name")
    my_data = []
    for stage in stages:
        my_data.append(fpkms.loc[t_name ,sex+stage])
    return my_data

def get_replicate_fpkm_data(ctab_data_dir,metadata_file,sex_):
    fpkm = [ ]
    for i, line in enumerate(open(metadata_file)):
        if i == 0:
            continue
        fields = line.split(",")
        srr_id = fields[0]
        sex = fields[1]
        if sex != sex_:
            continue
        stage = fields[2]
        ctab_path = os.path.join(ctab_data_dir, srr_id, 
                                "t_data.ctab")
        df = pd.read_csv(ctab_path, sep="\t", 
                                  index_col="t_name")
        fpkm.append(df.loc["FBtr0331261","FPKM"])
    return fpkm

male_rep_data = get_replicate_fpkm_data(sys.argv[5],sys.argv[4],"male")
female_rep_data = get_replicate_fpkm_data(sys.argv[5],sys.argv[4],"female")

male_data = sort_sex('male')
female_data = sort_sex('female')
labelz=['Male', 'Female',"Male rep","Female rep"]
labelzz=['10', '11', '12', '13', '14A', '14B', '14C', '14D']

fig, ax = plt.subplots()
ax.plot(male_data, color='blue')
ax.plot(female_data, color='red')

ax.plot(range(4,8),male_rep_data,'x')
ax.plot(range(4,8),female_rep_data,'x')

plt.xlabel("Developmental Stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.legend(labels= labelz, loc = 'center left', bbox_to_anchor=(1, 0.5))
plt.title("Male and Female mRNA abundance")

ax.set_xticklabels(labelzz, rotation = 'vertical')
ax.set_xticks(np.arange(len(labelzz)))

plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)