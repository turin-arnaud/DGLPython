# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:10:54 2021

@author: Arnaud
"""

def draw_triangle(heigh):
    for i in range(heigh-1):
        print(" "*(heigh-1-i) + "/" + " "*(2*i) + "\\")
    print("/" + "_"*(2*heigh-2) + "\\")
          

for heigh in range(1,10):
    draw_triangle(heigh)