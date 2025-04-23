#import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read in the csv file
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')

#Show the third column (the year) for the first 10 rows (inclusive)
print("The third column (the year) for the first 10 rows:")            
print(dalys_data.loc[:9,'Year']) 

#Shown the 10th year
print(f"\nThe 10th year with DALYs data recorded in Afghanistan: {dalys_data[dalys_data['Entity'] == 'Afghanistan'].at[9, 'DALYs']}")

#The DALYs for countries in 1990:
print('\nDALYs for all countries in 1990:')
series_select = (dalys_data['Year'] == 1990)
print(dalys_data[series_select])

#Show the mean value of DALYs in the UK and France
UK_mean_DALY = dalys_data[dalys_data["Entity"] == 'United Kingdom']['DALYs'].mean()
France_mean_DALY = dalys_data[dalys_data["Entity"] == 'France']['DALYs'].mean()         #Extract the DALYs values and calculate their means
print(f'\nMean DALYs in the UK (rounded to a 2 point scale): {UK_mean_DALY:.2f}')
print(f'Mean DALYs in France (rounded to a 2 point scale): {France_mean_DALY:.2f}')     #Print their values
if UK_mean_DALY > France_mean_DALY:
    print('DALYs mean in the UK is larger than France.')
elif UK_mean_DALY == France_mean_DALY:
    print('The DALYs means in the UK and France are the same.')
else:
    print('DALYs mean in the UK is less than France.')

#Plot the change of DALYs in the UK
df_UK = dalys_data[dalys_data["Entity"] == 'United Kingdom'].sort_values('Year')        #First sort the series according to values in the 'Year' column
plt.figure(figsize = (10, 6))                                                           #Plot the figure
plt.plot(df_UK['Year'], df_UK['DALYs'])
plt.xlabel('Year')
plt.ylabel('Disability-Adjusted Life Years (DALYs) in the UK')
plt.title('Trends in Disability-Adjusted Life Years (DALYs) in the United Kingdom over Time')
plt.show()

#Find entities that had a total DALYs value below 20,000 in any single year,
# and what were the corresponding years and DALYs values?
print('The entities that had a total DALYs value below 20,000 (with the year and DALYs values): ')
print(dalys_data[dalys_data['DALYs'] <= 20000][['Entity', 'Year', 'DALYs']])