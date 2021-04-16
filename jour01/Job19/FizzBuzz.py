# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:47:22 2021

@author: Arnaud
"""

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
