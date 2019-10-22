# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:56:18 2019

@author: jose
"""

def f(x): # name x used as a formal parameter
        y = 1
        x += y
        print('>>> Inside the function')
        print('x =', x)
        print('>>> Inside the function')
        return x

x = 3
y = 2
z = f(x) # value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)

def m():
    print(x)

def p(x):
    print(x)
    x = 1
    
x = 3
m()
x = 3
p(x)