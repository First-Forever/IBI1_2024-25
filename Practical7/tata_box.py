#import necessary libraries
import re

box_read = open('./Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') 
genes = box_read.readlines()                                                #Read every row of the file
box_read.close()                                
genes_names = []
genes_seq = []                                                              #Initialize the lists to store genes' names and genes' sequences after reading
line = len(genes)
i = 0
while i < line:                                                             #Extract all genes and their names
    if genes[i][0] == '>':
        genes_names.append(genes[i])
        seq = ''
        i += 1
        while i < line and genes[i][0] != '>':
            seq += genes[i]
            i += 1
        genes_seq.append(seq)
exam_seq = r'TATA[AT]A[AT]'                                                 #Prepare to extract the box sequence
box_write = open('tata_genes.fa', 'w')                                      #Open the writing file
ans_length = len(genes_names)                                               
for i in range(ans_length):                                                 #Starting the loop to scan every strings in the file, and find valid sequences
    gene_name = re.search(r'^>(\S+)\s+', genes_names[i]).group(1)
    gene_name = re.sub('_mRNA', '', gene_name)                              #Delete the _mRNA if it is in the name
    gene_seq = re.sub('\n', '', genes_seq[i])                                                 
    if re.search(exam_seq, gene_seq):                                       #Judge if exam sequence is in the current sequence
        box_write.write('>'+gene_name+'\n')
        box_write.write(gene_seq+'\n')                                       #Write valid sequences into the file
box_write.close()