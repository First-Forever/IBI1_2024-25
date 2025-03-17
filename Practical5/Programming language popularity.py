import matplotlib.pyplot as plt                                 #import the library used for plotting

language = {'Javascript': 62.3, 'HTML': 52.9, 'Python': 51, 
            'SQL': 51, 'Typescript': 38.5}                      #Define the dictionary
plt.figure(figsize = (10, 10))                                  #I don't know what is that
plt.bar(x = language.keys(), height = language.values())        #I hope that can give the keys and values of the following dictionary
plt.xlabel('Programming languages')
plt.ylabel('Percentage of Developers (%)')                      #Draw the label of x and y axis
plt.show()                                                      #Show the graph in another window

'''
Authorization:
Homework: Practical5: Programming language popularity
Author: Li Muxuan
Time last edited: 2025.03.17
All rights reserved.
'''