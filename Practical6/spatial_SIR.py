#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Initialization
beta = 0.3                          #infection probability
gamma = 0.05                        #recovery probability
population = np.zeros((105, 105))               #make array of all susceptible population
outbreak = np.random.choice(range(100), size = 2)   #Give an outbreak coordinate
population[outbreak[0], outbreak[1]] = 1
#Record the coordinate of all infected persons, in order to reduce repeating time 
# (Reason for using set variable: avoid repeat when adding infected coordinates. Otherwise, it will fall into infinity loop.)
infected = set([(outbreak[0], outbreak[1])])    
time = 100                          #Repeat time
nrows = 2
ncols = int(time/10/2) + 1
fig, ax = plt.subplots(nrows = nrows, ncols = ncols, figsize = (20, 6))
#Reminder: Dear teacher, I know that numpy.where() can satisfy the demand, but the time complexity will be a lot higher for system to find the infected coordinate.
#In this case, I will record all the infected persons' coordinates to avoid that.
'''
pseudocode:
(in the map, 0 is susceptible, 1 is infected, 2 is recovered)
Repeat:
    Extract the infected coordinate and repeat:
        Give a roll of random numbers to indicate surrounding susceptible persons infected.
        Examine the surrounding points are in the valid rage, 
        and add susceptible persons (marked as 0) into infected list and mark them as 1;
        Give a random number with probability gamma to recover;
Plot the map;
'''
for i in range(time+1):
    now_infected = list(infected.copy())        #Give a copy of infected persons
    for x, y in now_infected:
        step_infected = np.random.choice(a = 2, size = 9, p = [1 - beta, beta]).reshape((3, 3))     #Generate a group of ramdom numbers that are infected (reshape into (3, 3) so as to match with original map)
        for dx in np.arange(-1, 2):
            for dy in np.arange(-1, 2):         #Go through all infected individuals generated above and match them into original map
                if x+dx >= 0 and x+dx <= 100 and y+dy >=0 and y+dy <=100 and \
                    population[x+dx, y+dy] == 0 and step_infected[dx+1, dy+1] == 1:     #Make sure that the coordinate waiting to be appended are in the valid range, and original individual is susceptible
                    infected.add((x+dx, y+dy))
                    population[x+dx, y+dy] = 1
        if np.random.choice(a = 2, p = [1 - gamma, gamma]):     #Generate a random number for recovery for the given infected individual, and if recovered, move it out of the set
            population[x, y] = 2
            infected.discard((x, y))
    if(i % 10 == 0):
        figrow = int(i/10)// ncols
        figcol = int(i/10)%ncols
        ax[figrow, figcol].imshow(population[0:101, 0:101], cmap = 'viridis', interpolation = 'nearest')
        ax[figrow, figcol].set_title(f'Time {i}')
        #ax[figrow, figcol].axis('off')
if time // 10 % 2 == 0:
    ax[nrows-1, ncols-1].set_visible(False)
plt.suptitle('Infection Map')
plt.show()                                       #Plot the infection map
'''
Authorization:
Homework: Practical6: Looking at disease spread in 2D
Author: Li Muxuan
Time last edited: 2025.03.25
All rights reserved.
'''