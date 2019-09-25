# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:41:40 2019

@author: jose
"""

def fact_rec(n):
    print('start the function call ' + str(n))
    if n == 0:
        result = 1
        print('return the function call ' + str(n))
        return result
    else:
        result = n * fact_rec(n - 1)
        print('return the function call ' + str(n))
        return result
    
    
print('>>>', fact_rec(5))