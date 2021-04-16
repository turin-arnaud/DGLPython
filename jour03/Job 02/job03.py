# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:36:18 2021

@author: Arnaud
"""

import re

taille = int(input("Entre un nombre entier\n"))

f = open("data.txt", "r")
txt = f.read()
liste_de_mot = re.split("\s", txt)
nombre_de_mot = 0
for mot in liste_de_mot:
    if len(mot) == taille:
        nombre_de_mot += 1

print(nombre_de_mot)