conda install plink

*double click on the files to unzip it*

plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pca 2 --allow-extra-chr --allow-no-sex --mind

 plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno clean.txt --allow-no-sex --allow-extra-chr --assoc --all-pheno
 