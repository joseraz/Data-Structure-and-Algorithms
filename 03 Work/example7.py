# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:39:24 2019

@author: jose
"""
def f(x , y):
    for char in x[y]:
        print(char.isupper())
    if char == True:
        count += 1
    return count


print(f(['HEY YOU', 'date1', 100, 10, 'id'],0)) #6
print(f(['hey YOU', 'date1', 100, 10, 'id'],0)) #3