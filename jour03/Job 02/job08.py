# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:30:49 2021

@author: Arnaud
"""

import re
import matplotlib.pyplot as plt



"""
Lecture du texte
"""
f = open("data.txt", "r")
txt = f.read()
liste_de_mot = re.split("\s", txt)

"""
Calcule du nommbre d'occurence pour chaque taille de mot
"""

nombre_de_mot = [0 for i in range(19)]

for taille in range(1, 20):
    for mot in liste_de_mot:
        if len(mot) == taille:
            nombre_de_mot[taille-1] += 1
            
#print(nombre_de_mot)


"""
Calcule du pourcentage
"""
pourcentage = []
total = sum(nombre_de_mot)
for i in range(19):
    pourcentage.append(nombre_de_mot[i]/total*100)

print(pourcentage)

"""
Génération de l'histogramme'
"""
ind = range(1, 20)
fig, ax = plt.subplots()
p = ax.bar(ind, pourcentage)
ax.set_title('Pourcentage d’apparition de chaque taille de mot')
ax.set_xticks(ind)
ax.set_xticklabels(range(1, 20))
plt.show()
