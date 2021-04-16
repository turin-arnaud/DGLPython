# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:17:35 2021

@author: Arnaud
"""

import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Runtrack1"
    )

curseur = connexion.cursor()

#auteur_in = input("renseigner le nom d'un auteur")

curseur.execute("SELECT * FROM Auteur")
auteurs = curseur.fetchall()

for auteur in auteurs:
    print(auteur)