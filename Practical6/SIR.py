#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Initialization
N = 10000                            #sum of all population
infected = 1                        #infected population
susceptible = N-infected            #susceptible population
beta = 0.3                          #infection probability
gamma = 0.05                        #recovery probability
situation = np.zeros(shape = (5, 1005), dtype = int)          #track different population
situation[0, 0] = infected
situation[1, 0] = susceptible
situation[2, 0] = 0

#Time Course
'''
pseudocode:
Repeat 1000 times:
    Choose group of people in susceptible group to be infected (each individucal at probability beta*[proportion of the infected], dependent to each other);
    Choose group of people in infected group to recover (each individual at probability gamma, dependent to each other);
    Add infected susceptible people into the infected part of ndarray;
    Subtract infected susceptible people out of the susceptible part of ndarray;
    Add recovered people into the recovered part of ndarray;
    Subtract recovered people from the infected part of ndarray;
Plot the data
'''
time = 1000
for i in range(time):
    current_infected = situation[0, i]
    current_susceptible = situation[1, i]
    current_recover = situation[2, i]                                #Give the infected/susceptible population at current time
    p_infect = beta*current_infected/N                               #Calculate infected rate of susceptible population 
    step_infect = np.random.choice(a = range(2), size = current_susceptible, p = [1-p_infect, p_infect]) 
    #alternative: step_infect = np.random.binomial(n = current_susceptible, p = p_infect)?
    step_recover = np.random.choice(a = range(2), size = current_infected, p = [1 - gamma, gamma])  #Randomly choose infected and recovered people
    situation[0, i+1] = current_infected + (step_infect != 0).sum() - (step_recover).sum()
    situation[1, i+1] = current_susceptible - (step_infect != 0).sum()
    situation[2, i+1] = current_recover + (step_recover != 0).sum()                     #Update the ndarray'
    '''
    Write for fun:
    step_infect = np.random.binomial(n = current_susceptible, p = p_infect)
    step_recover = np.random.binomial(n = current_infected, p = gamma)
    situation[0, i+1] = current_infected + step_infect - step_recover
    situation[1, i+1] = current_susceptible - step_infect
    situation[2, i+1] = current_recover + step_recover'
    '''
plt.figure(figsize = (20, 10), dpi = 150)
plt.plot(np.arange(1, 1001), situation[0, 1:1001], label = 'Infected')
plt.plot(np.arange(1, 1001), situation[1, 1:1001], label = 'Susceptible')
plt.plot(np.arange(1, 1001), situation[2, 1:1001], label = 'RecoveredRecovered')
plt.title(f'SIR Model Display in {time} Days (Infection Rate: {beta}, Recovery Rate: {gamma})')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend(loc = 'upper right')
plt.show()
title = str(f'SIR Model Display in {time} Days (Infection Rate {beta}, Recovery Rate {gamma})')
plt.savefig(title, format = 'png')
'''
Authorization:
Homework: Practical6: A simple SIR model
Author: Li Muxuan
Time last edited: 2025.03.25
All rights reserved.
'''