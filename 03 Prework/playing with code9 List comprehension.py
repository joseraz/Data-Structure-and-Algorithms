# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 07:10:07 2019

@author: jose
"""

L = [ x**2 for x in range(1,7) ]
print(L)
# what are the tuples?
mixed = [ 1, 2, 'a', 3, 4.0 ]
print( [ x**2 for x in mixed if type(x) == int ] )

