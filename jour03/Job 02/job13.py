# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:04:18 2021

@author: Arnaud
"""

import re
import string
import matplotlib.pyplot as plt


"""
Des listes contennant l'alphabet en minuscule et en majuscule
"""
lowercase_alphabets = list(string.ascii_lowercase)



"""
Lecture du texte
"""
f = open("data.txt", "r")
txt = f.read()
txt = txt.lower()
liste_de_mot = re.split("\s", txt)

"""
Calcule du nommbre d'occurence pour chaque lettre
"""
liste_occurence = [0 for i in range(26)]

for i in range(26):
    for mot in liste_de_mot:
        if mot and mot[0] == lowercase_alphabets[i]:
            liste_occurence[i] += 1



"""
Calcule du pourcentage d'apparition de chaque lettre
"""
pourcentage = []
total = sum(liste_occurence)
for i in range(26):
    pourcentage.append(liste_occurence[i]/total*100)

print(pourcentage)

"""
Génération de l'histogramme'
"""
ind = range(1, 27)
fig, ax = plt.subplots()
p = ax.bar(ind, pourcentage)
ax.set_title('Pourcentage de présence de chaque lettre en début de mot')
ax.set_xticks(ind)
ax.set_xticklabels(lowercase_alphabets)
plt.show()
