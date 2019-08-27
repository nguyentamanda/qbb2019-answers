head -n 40000 SRR072893.fastq > SRR072893.10k.fastq

fastqc SRR072893.10k.fastq 

hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893-hisat2.sam

samtools sort -o SRR072893-hisat.bam SRR072893-hisat2.sam

samtools index SRR072893-hisat.bam 

stringtie SRR072893-hisat.bam  -G ../genomes/BDGP6.Ensembl.81.gtf -e -B -p 4 -o output.gtf





