#import necessary libraries
from Bio.Align import substitution_matrices

#Load Fasta files
random_file = open('random.fasta')
human_file = open('P04179.fasta')
mouse_file = open('P09671.fasta')

def skip_1row(file):
    seq = ""
    rows = file.readlines()
    for row in rows[1:]:
        seq += row
    return seq

random = skip_1row(random_file)
human = skip_1row(human_file)
mouse = skip_1row(mouse_file)

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