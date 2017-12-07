from Bioinformatics import DNA as BioDNA
from Bio import SeqIO

dna = {}
dnaGC = {}
for seq_record in SeqIO.parse("assets/rosalind_gc.txt", "fasta"):
    dna[str(seq_record.id)] = str(seq_record.seq)

for id, seq in dna.items():
    countA, countC, countG, countT = BioDNA.Nucleotide_Count(seq)
    dnaGC[str(id)] = BioDNA.GCCompute(countG, countC, len(seq))

maximum = max(dnaGC, key=dnaGC.get)  # Just use 'min' instead of 'max' for minimum.

print(maximum)
print(dnaGC[maximum])
