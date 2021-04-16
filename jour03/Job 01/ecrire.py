# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:26:41 2021

@author: Arnaud
"""

inputString = input("Ecrire une phrase\n")
f = open("output.txt", "a")
f.write(inputString)
f.close()