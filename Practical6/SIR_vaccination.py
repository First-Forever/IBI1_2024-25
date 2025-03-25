#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Initialization
N = 10000                            #sum of all population
infected = 1                        #infected population
beta = 0.3                          #infection probability
gamma = 0.05                        #recovery probability
start_ratio = 0.10
end_ratio = 1.00
gradient = 0.10                     #Give the trial interval for different vaccination ratio
plt.figure(figsize = (20, 10), dpi = 150)
for vaccine_ratio in np.arange(start_ratio, end_ratio, gradient):
    vaccined = int(vaccine_ratio*N)                               #Initialize vaccinated population
    susceptible = N-vaccined-infected                             #Give respective susceptible population
    situation = np.zeros(shape = (5, 1005), dtype = int)          #track different population
    situation[0, 0] = infected
    situation[1, 0] = susceptible
    situation[2, 0] = vaccined
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
    plt.plot(np.arange(1, 1001), situation[0, 1:1001], label = f'{vaccine_ratio:.0%}', color = cm.viridis(vaccine_ratio))
plt.plot(np.arange(1, 1001), np.zeros(shape = 1000), label = f'{end_ratio:.0%}', color = cm.viridis(end_ratio))  
plt.title(f'SIR Model Display with Different vaccine rate')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend(loc = 'upper right')
plt.show()
'''
Authorization:
Homework: Practical6: The efect of vaccination
Author: Li Muxuan
Time last edited: 2025.03.25
All rights reserved.
'''