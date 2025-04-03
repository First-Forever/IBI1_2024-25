#import necessary libraries
import re
import sys

input_seq = input("Input the splice that you want to count: ")      #Input the sequence to check
box = r'TATA[AT]A[AT]'                                              #Box sequence
if input_seq not in ('GTAG', 'GCAG', 'ATAC'):                       #Judge if it is valid; if not, stop the program
    print('Sequence not valid!')
    sys.exit()
read_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
genes_names = []
genes_seq = []                                                       #Initialize the lists to store genes' names and genes' sequences
genes = read_file.readlines()                                       #Read in the file
exam_seq = input_seq[0: 2] + r'\S*' + input_seq[2:]
write_file = open(f'{input_seq}_spliced_genes.fa', 'w')             #Start writing the sequences
line = len(genes)
i = 0
while i < line:                                                     #Extract all genes and their names
    if genes[i][0] == '>':                                          #Find the gene names
        now_gene_name = genes[i]
        now_gene_name = re.search(r'gene:(\S+)\s+', now_gene_name).group(1)
        seq = ''
        i += 1
        while i < line and genes[i][0] != '>':                      #Find the sequences
            seq += genes[i]
            i += 1
        now_gene_seq = seq
        now_gene_seq = re.sub('\n', '', now_gene_seq)                 
        if re.search(box, now_gene_seq) and re.search(exam_seq, now_gene_seq):           #Judge if it contains required gene sequence
            now_gene_name += f'_count: {len(re.findall(box, now_gene_seq))}\n' #Count the number of TATA boxes in the sequence
            write_file.write('>' + now_gene_name + now_gene_seq + '\n')          #If valid, write in a file
read_file.close()
write_file.close()