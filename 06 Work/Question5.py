# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:45:19 2019

@author: jose
"""

print([x**2 for x in range(2)])
print([len(name) for name in ['Joe', 'Mary']])

names = {name:len(name) for name in ['Joe', 'Mary', 'Zoe']}
print(names['Zoe'])

#names = [name:len(name) for name in ['Joe', 'Mary', 'Zoe']]
print(names['Zoe'])

x = {s for s in 'John'}
print(x)
print('j' in x) #this looks for 'j' inside of s