'''
pseudocode:
Define sum as zero;
Repeat:(define a number i that increase 1 after every loop)
    add the i into the sum;
    print the value of sum;
'''

sum = 0                         #initialize every "t" as zero
for i in range(1, 11):          #give the for cycle, start = 1, end = 11
    sum+=i                      #add every line number into sum
    print(sum, end = ' ')       #output every outcome