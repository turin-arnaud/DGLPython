# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:11:31 2021

@author: Arnaud
"""

import re

f = open("data.txt", "r")
txt = f.read()
liste_de_mot = re.split("\s", txt)
nombre_de_mot = len(liste_de_mot)
print(nombre_de_mot)


