# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:21:33 2019

@author: jose
"""

def square_root(x):
    guess = x/2
    eps = 0.01
    while abs(guess**2-x) >= eps:
        print(round(guess,2))
        guess = (guess + x/guess)/2
        print('new guess', round(guess,2))
    return guess

z = 20
print(round(square_root(20),2))