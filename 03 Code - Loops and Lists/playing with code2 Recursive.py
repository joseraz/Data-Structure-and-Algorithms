# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:26:12 2019

@author: jose
"""

def factrR(n):
    if n == 1:
        return n
    else:
        return n*factrR(n - 1)
    
print(factrR(5))