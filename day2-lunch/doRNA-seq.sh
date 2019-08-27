#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
	echo "*** Processing $SAMPLE"
	cp ../rawdata/$SAMPLE.fastq .
	fastqc $SAMPLE.fastq
	hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE-hisat2.sam
	samtools sort -o $SAMPLE-hisat2.bam $SAMPLE-hisat2.sam
	samtools index $SAMPLE-hisat.bam
	stringtie $SAMPLE-hisat.bam -G $ANNOTATION -e -B -p $THREADS -o $SAMPLE-output.gtf
done