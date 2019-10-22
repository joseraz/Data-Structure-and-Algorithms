# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 07:19:40 2019

@author: jose
"""

def applyToEach(L,f):
    """Assumes L is a list, f a function
        Mutates L by replacing each element, e of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.33]
print('L = ', L)
print('Apply abs to each element of L.')
applyToEach(L, abs) #abs is for absolute values
print('L = ', L) #funky stuff I can take function as parameters in a function

print('Apply int to each element of L.')
applyToEach(L, int)
print('L = ', L)
""" I need my factorial definition
print('Apply factorial to each element of L.')
applyToEach(L, factR)
print('L = ', L)"""
