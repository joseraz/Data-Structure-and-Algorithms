# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:50:35 2019

@author: jose
"""

def f(x):
    y = x -1
    z = y*2
    return y+z
y = 1
z = 2
x = 3
y = f(z+x)
print(x, y, z)