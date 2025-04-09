import sys                 #Import necessary libraries

canonical_seq = ('A', 'G', 'C', 'T')
def sequence_check(seq, restrict):                                          #Check if the sequences are valid
    for i in seq:
        if i not in canonical_seq:
            print("DNA sequence to be cut not valid! Input it again!")
            sys.exit()
    for i in restrict:
        if i not in canonical_seq:
            print("Recognition sequence of restriction enzyme not valid! Input it again!")
            sys.exit()

def find_cut_site(seq, restrict):                                           #Find the index of restriction enzyme
    ans = []                                                                #Initialize the answer list
    len_restrict = len(restrict)
    for i in range(len(seq)):                                               #Scan through all sites
        if seq[i:i+len_restrict] == restrict:
            ans.append(i)                                                   #If restriction enzyme sequence is found, add the index to the answer list
    return ans

#Now we give an example to show how to use the function 
seq = 'AGCTTTAGCTGGAGCTT'
len_seq = len(seq)
restrict = 'AGCT'            
sequence_check(seq = seq, restrict = restrict)                                          #Check sequences' validity
print(f'Cutting site of the given restriction enzyme is: {find_cut_site(seq, restrict)}')   #Output the results