#import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read in the csv file
delys_data = pd.read_csv('dalys-rate-from-all-causes.csv')

#Show the third column (the year) for the first 10 rows (inclusive)
print("The third column (the year) for the first 10 rows:")            
print(delys_data.loc[:9,'Year'])

#Shown the 10th year
print("\nThe 10th year with DALYs data recorded in Afghanistan:")
print(delys_data[delys_data['Entity'] == 'Afghanistan'].at[9, 'DALYs'])

#The DALYs for countries in 1990:
print('\nDALYs for all countries in 1990:')
print(delys_data[delys_data['Year'] == 1990][['Entity', 'DALYs']])

#Show the mean value of DALYs in the UK and France
UK_mean_DALY = delys_data[delys_data["Entity"] == 'United Kingdom']['DALYs'].mean()
France_mean_DALY = delys_data[delys_data["Entity"] == 'France']['DALYs'].mean()         #Extract the DALYs values and calculate their means
print(f'\nMean DALYs in the UK (rounded to a 2 point scale): {UK_mean_DALY:.2f}')
print(f'Mean DALYs in France (rounded to a 2 point scale): {France_mean_DALY:.2f}')     #Print their values

#Plot the change of DALYs in the UK
df_UK = delys_data[delys_data["Entity"] == 'United Kingdom'].sort_values('Year')        #First sort the series according to values in the 'Year' column
plt.figure(figsize = (10, 6))                                                           #Plot the figure
plt.plot(df_UK['Year'], df_UK['DALYs'])
plt.xlabel('Year')
plt.ylabel('Disability-Adjusted Life Years (DALYs) in the UK')
plt.title('Trends in Disability-Adjusted Life Years (DALYs) in the United Kingdom over Time')
plt.show()

#Find all countries with a less than 20000 DALYs in a certain year
print('The countries that have less than 20000 DALYs in a certain year:')
print(delys_data[delys_data['DALYs'] <= 20000])