import matplotlib.pyplot as plt                                 #import the library used for plotting

data = {'Javascript': 62.3, 'HTML': 52.9, 'Python': 51, 
            'SQL': 51, 'Typescript': 38.5}                      #Define the dictionary
print(data)
languages = ['Python', 'SQL']
for language in languages:
    print(f'The percentage of developers of {language}: {data[language]}')

plt.figure(figsize = (10, 10))                                  #I don't know what is that
plt.bar(x = data.keys(), height = data.values())        #I hope that can give the keys and values of the following dictionary
plt.xlabel('Programming languages')
plt.ylabel('Percentage of Developers (%)')                      #Draw the label of x and y axis
plt.show()                                                      #Show the graph in another window

'''
Pseudocode:
Import required libraries;
Define the dictionary;
Print the dictionary;
Define the required languages to output;
Print the percentage of Developers of the required languages;
Draw the bar plot of the languags and its percentage;
(need: label of x and y axis, language names, percentage of names)
Show the plot;
'''

'''
Authorization:
Homework: Practical5: Programming language popularity
Author: Li Muxuan
Time last edited: 2025.03.17
All rights reserved.
'''