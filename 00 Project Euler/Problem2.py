# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:48:57 2019

@author: jose
"""

from time import process_time 

def fib(n):
    """ Assumes n >= 0
    Returns Fibonacci of n.
    For project Euler I need term up to term 32."""
    if n == 0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#count to 32 in fibonacci for less than 4 million
def count_even_fib(n):
    start = process_time() 
    sum_of_fib = 0
    for i in range(n+1):
        x = fib(i)
        if x%2 == 0:
            #print('number ', i, 'fib ', x)
            sum_of_fib +=x
    return sum_of_fib, start
 
stop = process_time()
print(count_even_fib(32))  
print("Time:", stop-start)  