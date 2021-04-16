# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:35:24 2021

@author: Arnaud
"""

maliste = [0 for i in range(5)]

for i in range(5):
    maliste[i] = input("Entrez un nombre entier :\n")

print(maliste)
maliste.sort()
print(maliste)