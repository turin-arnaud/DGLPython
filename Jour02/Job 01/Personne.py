# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:06:31 2021

@author: Arnaud
"""

class Personne:
    def __init__(self, leNom, lePrenom):
        self.__nom = leNom
        self.__prenom = lePrenom
        
    def SePresenter(self):
        print("Je m'appelle", self.__prenom, self.__nom)
        
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def set_nom(self, nom):
        self.__nom = nom
        
    def set_prenom(self, prenom):
        self.__prenom = prenom   




P1 = Personne("Honnold", "Alex")
P1.SePresenter()
