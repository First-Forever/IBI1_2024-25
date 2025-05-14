#import necessary libraries
from Bio.Align import substitution_matrices

#Load Fasta files
random_file = open('random.fasta')
human_file = open('P04179.fasta')
mouse_file = open('P09671.fasta')

#Try skip the first information row
def skip_1row(file):
    seq = ""
    rows = file.readlines()
    for row in rows[1:]:
        seq += row.strip()
    return seq

random = skip_1row(random_file)
human = skip_1row(human_file)
mouse = skip_1row(mouse_file)

#Load blosum62 matrix alignment function
blosum62 = substitution_matrices.load("BLOSUM62")

#Try alignment of sequences, find score and identical percentage
def align_sequences(seq1, seq2):
    score = 0                   #Initialization
    cnt = 0
    L = len(seq1)
    for i in range(L):
        a1 = seq1[i]
        a2 = seq2[i]
        score += blosum62.get((a1, a2), blosum62.get((a2, a1), -4))     #Add score
        if a1 == a2:                                                    #Compare ammino acids
            cnt += 1                                                    #If amino acids are identical, add to cnt
    identity = cnt / len(seq1)
    return score, identity                                              #Return the score and identical percentage

for species1, species2 in [('random', 'human'), ('random', 'mouse'), ('human', 'mouse')]:   #Iterate all combinations
    score, identity = align_sequences(eval(species1), eval(species2))                       #Calculate the score and identical percentage
    print(species1.title() + '&' + species2.title() + ':')
    print(f"Score = {score}, Identity = {identity:.2%}\n")