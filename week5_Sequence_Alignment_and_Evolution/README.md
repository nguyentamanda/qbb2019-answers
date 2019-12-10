blastn -db nr -query week5_query.fa -out blastn-results.tsv -remote -evalue 1e-4 -max_target_seqs 1000

./00-fastamaker.py blastn-results.tsv > blastn.fasta
 
transeq -sequence blastn.fasta -outseq blastn_seq.tsv

mafft --auto blastn_seq.tsv > mafft.tsv

 ./01-parse_fasta.py < mafft.tsv > mafft.parsed.tsv
 
 ./01-parse_fasta.py < blastn-results.tsv > blastn-results.fasta.tsv 