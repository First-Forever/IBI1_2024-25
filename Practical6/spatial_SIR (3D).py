#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Initialization
beta = 0.3                          #infection probability
gamma = 0.05                        #recovery probability
population = np.zeros((105, 105, 105))               #make array of all susceptible population
outbreak = np.random.choice(range(100), size = 3)   #Give an outbreak coordinate
population[outbreak[0], outbreak[1], outbreak[2]] = 1
time = 100                          #Repeat time
nrows = 2
ncols = int(time/10/2) + 1
fig = plt.figure(figsize = (20, 6))
print(np.where(population == 1))
for i in range(time+1):
    now_infected_rows, now_infected_cols, now_infected_z = np.where(population == 1)        #Give a copy of infected persons
    now_infected = list(zip(now_infected_rows, now_infected_cols, now_infected_z))
    for x, y, z in now_infected:
        step_infected = np.random.choice(a = 2, size = (3, 3, 3), p = [1 - beta, beta])    #Generate a group of ramdom numbers that are infected (reshape into (3, 3) so as to match with original map)
        for dx in np.arange(-1, 2):
            for dy in np.arange(-1, 2):
                for dz in np.arange(-1, 2):         #Go through all infected individuals generated above and match them into original map
                    nx, ny, nz = x+dx, y+dy, z+dz
                    if nx >= 0 and nx <= 100 and ny >=0 and ny <=100 and nz >= 0 and nz <= 100 and \
                        population[nx, ny, nz] == 0 and step_infected[dx+1, dy+1, dz+1] == 1:     #Make sure that the coordinate waiting to be appended are in the valid range, and original individual is susceptible
                        population[nx, ny, nz] = 1
        if np.random.choice(a = 2, p = [1 - gamma, gamma]):     #Generate a random number for recovery for the given infected individual, and if recovered, move it out of the set
            population[x, y] = 2
    if(i % 10 == 0):
        ax = fig.add_subplot(nrows, ncols, i // 10 + 1, projection = '3d')
        infected_x, infected_y, infected_z = np.where(population[0:101, 0:101, 0:101] == 1)
        recovered_x, recovered_y, recovered_z = np.where(population[0:101, 0:101, 0:101] == 2)
        ax.scatter(infected_x, infected_y, infected_z, c='red', label='Infected')
        ax.scatter(recovered_x, recovered_y, recovered_z, c='green', label='Recovered')
        ax.set_title(f'Time {i}')
        ax.legend()
plt.suptitle('Infection Map')
plt.show()                                       #Plot the infection map
'''
Authorization:
Homework: Practical6: Looking at disease spread in 3D
Author: Li Muxuan
Time last edited: 2025.03.27
All rights reserved.
'''