# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:56:35 2021

@author: Arnaud
"""

def draw_rectangle(width, heigh):
    print("|" + "-"*width + "|")
    for i in range (heigh-2):
        print("|" + " "*width + "|")
    print("|" + "-"*width + "|")
    
draw_rectangle(10,3)