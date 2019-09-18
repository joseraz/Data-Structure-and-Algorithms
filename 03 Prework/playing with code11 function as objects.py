# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:49:14 2019

@author: jose
"""
# I do not get it
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)

#what does this function mean?
L = []
for i in map(lambda x, y: x**y, [ 1, 2, 3, 4 ], [ 3, 2, 1, 0]):
    L.append(i)
    print(L)
    
    
    