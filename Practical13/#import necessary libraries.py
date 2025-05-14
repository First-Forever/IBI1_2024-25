import pandas as pd

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
blosum62 = pd.read_csv('blosum62.csv', sep = ',', dtype = int)
blosum62.index = blosum62.columns


#Try alignment of sequences, find score and identical percentage
def align_sequences(seq1, seq2):
    score = 0
    cnt = 0
    L = len(seq1)
    for a1, a2 in zip(seq1, seq2):
        score += blosum62.loc[a1, a2]
        if a1 == a2:
            cnt += 1
    return score, cnt/L 

for species1, species2 in [('random', 'human'), ('random', 'mouse'), ('human', 'mouse')]:   #Iterate all combinations
    score, identity = align_sequences(eval(species1), eval(species2))                       #Calculate the score and identical percentage
    print(species1.title() + '&' + species2.title() + ':')
    print(f"Score = {score}, Identity = {identity:.2%}\n")