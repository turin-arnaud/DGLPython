# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:05:59 2021

@author: Arnaud
"""

BLUE = "BLUE"
RED = "RED"
 
 
opponent = {BLUE: RED, RED: BLUE}
 
 
 
class Skins:
 
    BOAT = "X"
    DESTROYED_BOAT = "&"
    SEA = " "
    HIDDEN = "#"
 
 
class Position:
    """
    Des coordonnées
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def right(self):
        return Position(self.x, self.y + 1)
        
    def down(self):
        return Position(self.x + 1, self.y)
        
        

class Boat:
    """
    Un bateau
    """
 
 
    def __init__(self, position, size, orientation = "H"):
        self.occupied_positions = [position]
        if orientation == "H":
            for i in range(size-1):
                self.occupied_positions.append(position.right())
        elif orientation == "V":
            for i in range(size-1):
                self.occupied_positions.append(position.down())
        else:
            print("invalid orientation")
            
            
    def touched(self, touched_position):
        self.occupied_position.remove(touched_position)
        if not self.occupied_position:
            print("Coulé!")
 

 
class Board:
    """
    Le plateau de jeu
    """
 
 
    def __init__(self, size):
 
         self.content = [[" " for i in range(size)] for j in range(size)]
        
    """ Affiche le plateau de jeu """
    def display(self):
        for ligne in self.content:
            print(ligne)
    
    """ Place un bateau sur le plateau """
    def place_boat(self, boat):
        for position in boat.occupied_positions:
            self.content[position.x][position.y] = "X"
            
    
    
        
            

Board1 = Board(4)
boat1 = Boat(Position(0,3), 1)
boat2 = Boat(Position(1,0), 2)
Board1.place_boat(boat1)
Board1.place_boat(boat2)
Board1.display()
