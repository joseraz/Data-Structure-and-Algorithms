# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:31:08 2019

@author: jose
"""

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        

for i in map(fib, [2, 6, 4]):
    print(i)
