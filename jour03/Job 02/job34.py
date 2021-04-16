# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:59:08 2021

@author: Arnaud
"""

"""
Statistique taille de mot
"""

from random import *
import string

"""
Une liste contennant l'alphabet en minuscule
"""
alphabet = list(string.ascii_lowercase)

def pourcentage_cummule(pourcentage):
    for i in range(1, len(pourcentage)):
        pourcentage[i] += pourcentage[i-1]
        



def generateur_taille_aleatoire():
    pourcentage_taille = [0.8166284715445631, 11.439531397413072, 12.618963814205516, 14.659341839382764, 13.737886294158406, 11.33121008794395, 10.489695839558328, 8.010492934399558, 6.25962512815749, 4.833636025059636, 2.854108837774564, 1.4356195578342896, 0.8955470652254506, 0.32649798314414746, 0.1783764757819631, 0.05087948210312086, 0.030340193682933045, 0.02667550736729787, 0.004943065262949766]
    pourcentage_cummule(pourcentage_taille)
    #print(pourcentage_taille)
    n = random()*100
    #print(n)
    for i in range(len(pourcentage_taille)):
        if n < pourcentage_taille[i]:
            taille = i+1
            break
    return taille

print(generateur_taille_aleatoire())


def generateur_premiere_lettre():
    pourcentage_premiere_lettre = [8.775699061379232, 1.3784633229989807, 5.183608892376318, 5.3912057076330635, 11.566912445147617, 2.154520604026559, 0.7070573535244122, 2.579607920065844, 9.623144400898962, 0.0, 0.01407291475651725, 1.7347212923200268, 3.785955231072996, 6.9260063200180815, 2.393674864494889, 6.802676412515512, 8.088087917336551, 2.5717612039591797, 9.021505972459734, 3.3639383691624056, 2.2117504573697295, 5.618504603548933, 0.0, 0.021407888508398972, 0.0, 0.08571684442605962]
    pourcentage_cummule(pourcentage_premiere_lettre)
    
    n = random()*100
    
    for i in range(len(pourcentage_premiere_lettre)):
        if n < pourcentage_premiere_lettre[i]:
            ind_lettre = i+1
            break
    
    return alphabet[ind_lettre]

print(generateur_premiere_lettre())