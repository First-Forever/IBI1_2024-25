import matplotlib.pyplot as plt

uk_countries = [57.11, 3.13, 1.91, 5.45]
uk_countries_names = ['England', 'Wales', 'Northern Ireland', 'Scotland']
zhejiang_near_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
zhejiang_near_provinces_names = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']           #Define the populations and their names
print(f"Sorted UK countries' population: {sorted(uk_countries)}")
print(f"Sorted Provinces' population near Zhejiang: {sorted(zhejiang_near_provinces)}")         #Print the population values

plt.figure(figsize = (10, 10))                  
plt.pie(x = uk_countries, labels = uk_countries_names, autopct = '%.2f%%')                                          #I don't know what that means.
plt.axis('equal')
plt.title("UK countries' population (percentage)")                                                           #Draw the pie chart, with labels and title added
plt.show()                                                                                      #Show the plot
plt.figure(figsize = (10, 10))
plt.pie(x = zhejiang_near_provinces, labels = zhejiang_near_provinces_names, autopct = '%.2f%%')
plt.axis('equal')
plt.title("Provinces' population near Zhejiang (percentage)")                                                #Draw the pie chart again, with labels and title added
plt.show()                                                                                      #Show the plot again

'''
Pseudocode:
Define the uk country populations, uk country names, province populations near zhejiang province and their names;
Print the value of uk country populations;
Print the value of province populations near zhejiang province;
Dry two bar chart of the data above;
(including: title, their names)
Show the plot;
'''

'''
Authorization:
Homework: Practical5: Programming language popularity
Author: Li Muxuan
Time last edited: 2025.03.17
All rights reserved.
'''