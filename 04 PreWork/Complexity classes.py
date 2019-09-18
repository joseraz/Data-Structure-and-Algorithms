# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:47:37 2019

@author: jose
"""
#logarithmic complexity
def intToStr(i):
    """Assumes i is a non-negative int
    Returns a decimal string represention of i"""
    digits = '123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result 
        i = i//10
    return result

#