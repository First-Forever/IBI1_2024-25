# What does this piece of code do?
# Answer:  Counting the total number of attempts required to generate two identical random integers ranging from 1 to 5 after several loops.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0							#initialize the counter as zero
while progress>=0:					#start the loop (infinite)
	progress+=1						#add 1 into the counter
	first_n = randint(1,6)			#generate the first random integer
	second_n = randint(1,6)			#generate the second random integer
	if first_n == second_n:			#judge if the two variables are the same
		print(progress)				#if they are the same, print the total attempt number
		break						#exit the loop after finding the match

