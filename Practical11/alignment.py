#import necessary libraries
from Bio.Align import substitution_matrices
from Bio import SeqIO

#Load Fasta files
human = str(SeqIO.read("P04179.fasta", "fasta").seq)
mouse = str(SeqIO.read("P09671.fasta", "fasta").seq)
random = str(SeqIO.read("random.fasta", "fasta").seq)

blosum62 = substitution_matrices.load("BLOSUM62")

def align_sequences(seq1, seq2):
    score = 0
    cnt = 0
    L = len(seq1)
    for i in range(L):
        a1 = seq1[i]
        a2 = seq2[i]
        score += blosum62.get((a1, a2), blosum62.get((a2, a1), -4))
        if a1 == a2:
            cnt += 1
    identity = cnt / len(seq1)
    return score, identity

for species1, species2 in [('random', 'human'), ('random', 'mouse'), ('human', 'mouse')]:
    score, identity = align_sequences(eval(species1), eval(species2))
    print(species1.title() + '&' + species2.title() + ':')
    print(f"Score = {score}, Identity = {identity:.2%}\n")