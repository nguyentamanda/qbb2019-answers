wget http://67.207.142.119/outgoing/g1e.tar.xz

wget http://hgdownload.soe.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz

gunzip chr19.fa.gz

index the chr19.fa file 
bowtie2-build chr19.fa mouse19

use bowtie to align the reads
bowtie2 -x mouse19 -q g1e/CTCF_ER4.fastq -S CTCF_ER4.sam
bowtie2 -x mouse19 -q g1e/CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x mouse19 -q g1e/input_ER4.fastq -S input_ER4.sam
bowtie2 -x mouse19 -q g1e/input_G1E.fastq -S input_G1E.sam

samtools view -S -b CTCF_ER4.sam > CTCF_ER4.bam
samtools view -S -b CTCF_G1E.sam > CTCF_G1E.bam
samtools view -S -b input_ER4.sam > input.ER4.bam
samtools view -S -b input_G1E.sam > input_G1E.bam

macs2 callpeak -t CTCF_ER4.bam -c input.ER4.bam -g 81e6 --outdir CTCF_ER4
macs2 callpeak -t CTCF_G1E.bam -c input_G1E.bam -g 81e6 --outdir CTCF_G1E

./00-BED.py CTCF_ER4/NA_peaks.narrowPeak > CTCF_ER4/NA_peaks.narrowPeak.bed
./00-BED.py CTCF_G1E/NA_peaks.narrowPeak > CTCF_G1E/NA_peaks.narrowPeak.bed

#Differential binding  
bedtools intersect -v -a CTCF_G1E/NA_peaks.narrowPeak.bed -b CTCF_ER4/NA_peaks.narrowPeak.bed > intersect.bed
bedtools intersect -v -a CTCF_ER4/NA_peaks.narrowPeak.bed -b CTCF_G1E/NA_peaks.narrowPeak.bed > intersect2.bed

#Feature Overlap 
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b intersect.bed > annotationed.intersects.bed
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b intersect2.bed > annotationed2.intersects.bed

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b CTCF_ER4/NA_peaks.narrowPeak > CTCF_ER4.bedtools.tools
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b CTCF_G1E/NA_peaks.narrowPeak > CTCF_G1E.bedtools.tools




























