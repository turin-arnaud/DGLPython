# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:55:48 2021

@author: Arnaud
"""

import re
import string
import matplotlib.pyplot as plt


"""
Une liste contennant l'alphabet en minuscule
"""
alphabet = list(string.ascii_lowercase)



"""
Lecture du texte
"""
f = open("data.txt", "r")
txt = f.read()
txt = txt.lower()


"""
Calcule du nombre d'occurence pour chaque lettre
"""
matrice_occurence = [[0 for j in range(26)] for i in range(26)]

for ind_txt in range(len(txt)): #on parcourt le texte
    for i in range(26):
        if txt[ind_txt] == alphabet[i]: # Si le charactere est une lettre de l'alphabet
            for j in range(26):
                if txt[ind_txt + 1] == alphabet[j]: # On regarde quelle lettre est le charactere suivant
                    matrice_occurence[i][j] += 1


for line in matrice_occurence:
    print(line)

"""
Calcule du pourcentage d'apparition de chaque lettre
"""
pourcentage = [[0 for j in range(26)] for i in range(26)]
for i in range(26):
    total = sum(matrice_occurence[i])
    if total != 0:
        for j in range(26):
            pourcentage[i][j] = matrice_occurence[i][j]/total*100
        



"""
Génération de l'histogramme'
"""
ind = range(1, 27)
fig, ax = plt.subplots()
for i in range(26):
    ax.plot(alphabet, pourcentage[i], label = alphabet[i])

ax.set_title('Pourcentage d’apparition de chaque lettre la suivant')
ax.set_ylabel('%')
ax.legend()

plt.show()
