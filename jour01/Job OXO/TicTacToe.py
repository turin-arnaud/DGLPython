# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:31:48 2021

@author: Arnaud
"""

import pygame, sys
from pygame.locals import *
import numpy as np
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((600,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("TicTacToe1337")
 


class TicTacToe():
    def __init__(self):
        # matrice 3x3 vide qui sera rempli par les joueur
        self.matrice = [[0]*3 for i in range(3)]
        # Le joueur qui est en train de jouer
        self.player = 1
        # Le joueur gagnant, 0 si pas de gagnant
        self.winner = 0
        # Dessine la grille de jeu
        self.draw_grill()
        
        
    def play(self, pos):
        for i in range(3):
            for j in range(3):
                if pygame.Rect(200*i, 200*j, 200, 200).collidepoint(pos) and self.matrice[i][j] == 0:
                    self.matrice[i][j] = self.player
                    self.update(i,j)
                    print(self.matrice)
                    self.is_there_a_winner()
                    #print(self.winner)
                    self.change_player()
                    
    
    def update(self, i, j):
        self.matrice[i][j] = self.player
        X = 200*i+100
        Y = 200*j+100
        if self.player == 1:
            self.draw_cross(X,Y)
        elif self.player == -1:
            self.draw_circle(X,Y)
            
    def change_player(self):
        self.player = -self.player
        
    def is_there_a_winner(self):
        for i in range(3):
            if sum(self.matrice[i]) == 3:
                self.winner = 1
                pygame.draw.line(DISPLAYSURF, GREEN, (100+200*i, 20), (100+200*i,580), 20)
            elif sum(self.matrice[i]) == -3:
                self.winner = 2
                pygame.draw.line(DISPLAYSURF, RED, (100+200*i, 20), (100+200*i,580), 20)
        for j in range(3):
            if sum(self.matrice[i][j] for i in range(3)) == 3:
                self.winner = 1
                pygame.draw.line(DISPLAYSURF, GREEN, (20, 100+200*j), (580, 100+200*j), 20)
            elif sum(self.matrice[i][j] for i in range(3)) == -3:
                self.winner = 2
                pygame.draw.line(DISPLAYSURF, RED, (20, 100+200*j), (580, 100+200*j), 20)
        if sum(self.matrice[i][i] for i in range(3)) == 3:
            self.winner = 1
            pygame.draw.line(DISPLAYSURF, GREEN, (20, 20), (580, 580), 20)
        elif sum(self.matrice[i][i] for i in range(3)) == -3:
            self.winner = 2
            pygame.draw.line(DISPLAYSURF, RED, (20, 20), (580, 580), 20)
        if sum(self.matrice[i][2-i] for i in range(3)) == 3:
            self.winner = 1
            pygame.draw.line(DISPLAYSURF, GREEN, (20, 580), (580, 20), 20)
        elif sum(self.matrice[i][2-i] for i in range(3)) == -3:
            self.winner = 2
            pygame.draw.line(DISPLAYSURF, RED, (20, 580), (580, 20), 20)
            
    def draw_grill(self):
    # Drawing the grill
        pygame.draw.line(DISPLAYSURF, BLUE, (200,10), (200,590), 10)
        pygame.draw.line(DISPLAYSURF, BLUE, (400,10), (400,590), 10)
        pygame.draw.line(DISPLAYSURF, BLUE, (10,200), (590,200), 10)
        pygame.draw.line(DISPLAYSURF, BLUE, (10,400), (590,400), 10)

    def draw_cross(self,X,Y):
        pygame.draw.line(DISPLAYSURF, GREEN, (X-60,Y-60), (X+60,Y+60), 20)
        pygame.draw.line(DISPLAYSURF, GREEN, (X-60,Y+60), (X+60,Y-60), 20)
    
    def draw_circle(self,X,Y):
        pygame.draw.circle(DISPLAYSURF, RED, (X,Y), 60, 20)

T = TicTacToe()
 
# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # handle MOUSEBUTTONUP
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            T.play(pos)
            
   
    FramePerSec.tick(FPS)