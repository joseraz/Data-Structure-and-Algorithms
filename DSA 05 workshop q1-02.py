# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:27:14 2019

@author: jose
"""

def calculate(x):
    return len(x)

a = ['a', 'A', 'er', 'cere']
b = []
for i in a:
        b.append(calculate(i))

print(b)

a = [3,6,8,7]
b=[]
for i in range(len(a)):
    b.append(a[len(a)-1-i])
    print(b)
print(b)