# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:12:18 2019

@author: jose
"""

def fact(n):
    """Assumes n is a natural number
    Returns n!"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

print(fact(7))