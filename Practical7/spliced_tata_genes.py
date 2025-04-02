#import necessary libraries
import re
import sys

input_seq = input("Input the splice that you want to count: ")      #Input the sequence to check
if input_seq not in ('GTAG', 'GCAG', 'ATAC'):                       #Judge if it is valid; if not, stop the program
    print('Sequence not valid!')
    sys.exit()
read_file = open('tata_genes.fa', 'r')
genes = read_file.readlines()                                       #Read in the file
read_file.close()
exam_seq = input_seq[0: 2] + r'\S*' + input_seq[2:]
write_file = open(f'{input_seq}_spliced_genes.fa', 'w')             #Start writing the sequences
for gene in genes:
    if gene[0] == '>':
        now_gene_name = gene                                        #Find the gene names
    elif gene[0] != '>' and gene:                                           
        now_gene_seq = gene                                         #Find the sequences
        if re.search(exam_seq, now_gene_seq):                      #Judge if it contains required gene sequence
            write_file.write(now_gene_name + now_gene_seq)          #If valid, write in a file
write_file.close()