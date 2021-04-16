# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:54:23 2021

@author: Arnaud
"""

import re
import string
import matplotlib.pyplot as plt


"""
Des listes contennant l'alphabet en minuscule et en majuscule
"""
lowercase_alphabets=list(string.ascii_lowercase)
uppercase_alphabets=list(string.ascii_uppercase)


"""
Lecture du texte
"""
f = open("data.txt", "r")
txt = f.read()


"""
Calcule du nommbre d'occurence pour chaque lettre
"""
liste_occurence = []

for i in range(26):
    occurences_lowercase = re.findall(lowercase_alphabets[i], txt)
    occurences_uppercase = re.findall(uppercase_alphabets[i], txt)
    nombre_occurence = len(occurences_lowercase) + len(occurences_uppercase)
    liste_occurence.append(nombre_occurence)


"""
Calcule du pourcentage d'apparition de chaque lettre
"""
pourcentage = []
total = sum(liste_occurence)
for i in range(26):
    pourcentage.append(liste_occurence[i]/total*100)


"""
Génération de l'histogramme'
"""
ind = range(1, 27)
fig, ax = plt.subplots()
p = ax.bar(ind, pourcentage)
ax.set_title('Pourcentage d’apparition de chaque lettre')
ax.set_xticks(ind)
ax.set_xticklabels(lowercase_alphabets)
plt.show()
