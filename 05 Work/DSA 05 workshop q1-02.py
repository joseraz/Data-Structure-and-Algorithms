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
        print('b', b)
        print('calculate', calculate(i))
        b.append(calculate(i))
# I do not understand what is happening here.
        #Oh, its taking the length of each string and printing it out, duh.
print('>>>', b)

a = [3,6,8,7]
b=[]
for i in range(len(a)):
    b.append(a[len(a)-1-i])
    print(b)
print(b)