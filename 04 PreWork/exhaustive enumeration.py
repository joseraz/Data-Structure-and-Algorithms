# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:18:05 2019

@author: jose
"""

def squareRootExhaustive(x, epsilon):
    """Assumes x and epsilon are positive floats & epsilon < 1
    Returns y such that y*y is within epsilon of x"""
    step = epsilon**2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        print(ans)
        ans += step
    if ans*ans > x:
        raise ValueError #what is raise
    return ans

print(squareRootExhaustive(4, 0.2))