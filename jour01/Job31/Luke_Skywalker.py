# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:42:15 2021

@author: Arnaud
"""

from random import randint

def arrondit(notes):
    for i in range(len(notes)):
        if notes[i] > 40 and notes[i]%5 > 2:
            notes[i] = (int(notes[i]/5)+1)*5
    return notes


notes = []
for i in range(10):
    notes.append( randint(0, 100) )
print(notes)
print(arrondit(notes))