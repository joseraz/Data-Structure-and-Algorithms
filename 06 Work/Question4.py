# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:32:31 2019

@author: jose
"""

cities = set()
cities.add('London')
print('Rome' in cities)

cities = ('London', 'Paris')
#cities.add('Amsterdam')
print(cities)

cities = ('London', 'Paris', 'Rome')
#cities.append('Amsterdam')
print(cities)

#cities[0]=('Amsterdam')

def sum_diff(x, y):
    return x + y, x-y

z, w = sum_diff(5,3)
print(type(z))
