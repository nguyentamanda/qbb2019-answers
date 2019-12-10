sort the narrow peaks file for the top 100 scores
`sort -k 5 -n -r ER4_peaks.narrowPeak | head -n 100 > ER4_peaks.narrowPeak100`

bedtools getfasta -fi chr19.fa -bed ER4_peaks.narrowPeak100 > ER4_peaks.narrowPeakbed

meme-chip -meme-maxw 20 -memecER4_peaks.narrowPeakbed

tomtom memechip_out/combined.meme JASPAR_CORE_2016.meme