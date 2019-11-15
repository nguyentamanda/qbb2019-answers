Week 11 Command line 

conda create -n lab-week11 python=3.6 scanpy jupyter

conda activate lab-week11

wget https://bx.bio.jhu.edu/data/cmdb-lab/scrnaseq/neuron_10k_v3_filtered_feature_bc_matrix.h5

mate 01-Filtering.py
./01-Filtering.py, comment out the middle 4 lines to get the unfiltered plot 

mate 02-Clustering.py 
./02-Clustering.py

mate 03-Genes.py 
./03-Genes.py

mate 04-Cell_Tpes.py 
./04-Cell_Tpes.py 

'Malat1': mouse hippocampus neurons
'Ccna2': Neuronal intermediate progenitor cells
'mt-Atp6': Cholinergic enteric neurons
'Lhx6': Ivy and MGE-derived neurogliaform cells
'mt-Cytb': Excitatory neurons, cerebral cortex
'Zbtb20': Excitatory neurons, cerebral cortex
'Npas1': Hippocamposeptal projection, cortex/hippocampus
'Ftl1': Neuroblast-like, habenula
'Trem2': Microglia
'Reln': CGE-derived neurogliaform cells Cxcl14+, cortex/hippocampus
'Col3a1': Nitrergic enteric neurons


