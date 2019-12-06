Make a conda environment
conda create -n highfive -c bioconda -c anaconda -c conda-forge hifive

Activate the environment
conda activate highfive

download data and drag into the wd

hifive fends -B chr10_frags.bed FEND_NAME

hifive hic-data -M chr10_data.mat FEND_NAME DATA_NAME

python -c "import hifive; hic=hifive.HiC('PROJECT_NAME', 'w'); hic.load_data('DATA_NAME'); hic.filter_fends(10); hic.save()"

hifive hic-normalize express -w cis -f 10 PROJECT_NAME

hifive hic-heatmap -b 500000 -d raw -F npz -i IMAGENAME1.png PROJECT_NAME OUTPUT_NAME.npz

hifive hic-interval -c chr10 -s 5000000 -e 50000000 -b 50000 -d fend -M -i IMAGENAME.png PROJECT_NAME OUTPUT_NAME

Rvalue: 0.5835504406346801