# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:27:21 2019

@author: jose
"""


x = 'Hey you'
s = set(x) #Cool so the set() counts the space as a one thing.
print(s)
print(len(s))

s.update('hey')
print(s)  #Ok, so lower case h and upper case H are different.
print(len(s))

s = {'bird', 'cat', 'mouse'}
L = ['mouse', 'moose', 'dog', 'moose', 'mouse', 'moosemouse']
count = 0
for item in L:
    if item in s:
        count += 1
print(count)