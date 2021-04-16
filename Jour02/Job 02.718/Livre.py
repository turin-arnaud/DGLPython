# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:30:02 2021

@author: Arnaud
"""

from Personne import Personne

class Livre:
    
    def __init__(self, titre, Auteur):
        self.titre = titre
        self.Auteur = Auteur
        
    def print_titre(self):
        print(self.titre)
        
    def __eq__(self, other):
        return self.titre == other.titre and self.Auteur == other.Auteur
    
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.titre, self.Auteur))


        

class Auteur(Personne):
 
    def __init__(self, nom, prenom, oeuvre = []): 
        Personne.__init__(self, nom, prenom) 
        self.oeuvre = oeuvre #liste de Livre
        
    def listerOeuvre(self):
        for livre in self.oeuvre:
            livre.print_titre()
            
    def ecrireUnLivre(self, titre):
        nouveauLivre = Livre(titre, self)
        self.oeuvre.append(nouveauLivre)
    
    def existe_dans_oeuvre(self, titre):
        return titre in [livre.titre for livre in self.oeuvre]
    
    def __eq__(self, other):
        return self.get_nom == other.get_nom and self.get_prenom == other.get_prenom
    
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.get_nom, self.get_prenom))


# A1 = Auteur("Rolling", "J. K.")
# for i in range(1, 8):
#     A1.ecrireUnLivre("Harry Potter " + str(i))

# A1.listerOeuvre()
# print(A1.existe_dans_oeuvre("Harry Potter 1"))
# print(A1.existe_dans_oeuvre("Harry Potter 8"))
