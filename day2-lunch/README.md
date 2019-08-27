head -n 40000 SRR072893.fastq > SRR072893.10k.fastq

fastqc SRR072893.10k.fastq 

hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893-hisat2.sam

samtools sort -o SRR072893-hisat.bam SRR072893-hisat2.sam

samtools index SRR072893-hisat.bam 

stringtie SRR072893-hisat.bam  -G ../genomes/BDGP6.Ensembl.81.gtf -e -B -p 4 -o output.gtf

cut -f 3 SRR072893-hisat2.sam | grep -v "*" | grep -v "LN" | grep -v "SO" | grep -v "PN" | uniq -c | grep -v "21" | /
grep -v -i "unmapped" | grep -v "mapped" | grep -v "dmel" | grep -v "r"

3071588 X
12826 Y
2965008 2L
3562016 2R
3186807 3L
4133309 3R
