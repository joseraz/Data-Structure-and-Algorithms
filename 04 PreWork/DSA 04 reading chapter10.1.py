# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:24:54 2019

@author: jose
"""

def search(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        return False
    
def search2(L,e):
    """Assumes L is a list, the elements of which are in 
    asceding order.
    Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# missing last search algorithm
            