#import necessary libraries
import re

ans = []
def max_search(pattern, string, start):
    if start >= len(string):
        return
    now_string = string[start:]
    match = re.search(pattern = pattern, string = now_string)
    if match:
        ans.append(match.group())
        max_search(pattern, string, match.end())
    else:
        return
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
introns = re.findall(r'(GT.*AG)', seq)          #Find sequences of the introns
mmax = len(introns[0])       
index = introns[0]                                      #Initialize the variables for finding largest intron
for intron in introns[1:]:                          #Repeat for each intron in the list
    if len(intron) > mmax:
        mmax = len(intron)
        index = intron
print(f"The largest intron: {index}")                           #Print the results
print(f"The length of the largest intron: {mmax}")                          #Print the results