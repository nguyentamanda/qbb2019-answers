#!/usr/bin/env python3

""""
Create a time course of a given transript of females 

Usage: ./02-timecourse.py <t_names aka transcript id> <samples.csv> <FPKMs>
"""
import sys 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

#Specify transcript of interest 
t_name=sys.argv[1]

#Load metadata 
samples=pd.read_csv(sys.argv[2]) #load in the meta data 

def sort_sex(sex):
    soi = samples.loc[:,"sex"] == sex #filter for the samples of interest to only be for females 

    stages = samples.loc[soi, "stage"] #taking out the rows that are true and the samples 

    # print(srr_ids) #will print with the rownames

    #Load FPKMs 
    fpkms = pd.read_csv(sys.argv[3], index_col="t_name")

    my_data = []
    #Extract data 
    for stage in stages:
        # print(srr_id) #will only print the strings 
        my_data.append(fpkms.loc[t_name ,sex+stage]) #extract info from tname with corresponding srr_id and add it to a list, my data
    return my_data

male_data = sort_sex('male')
female_data = sort_sex('female')
labelz=['Male', 'Female']
labelzz=['10', '11', '12', '13', '14A', '14B', '14C', '14D']

fig, ax = plt.subplots()
ax.plot(male_data, color='blue')
ax.plot(female_data, color='red')
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.legend(labels= labelz, loc = 'center left', bbox_to_anchor=(1, 0.5))
plt.title("Male and Female mRNA abundance")

ax.set_xticklabels(labelzz, rotation = 'vertical')
ax.set_xticks(np.arange(len(labelzz)))

plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)