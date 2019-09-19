# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:59:58 2019

@author: jose
"""

L = ['Mark', 'Shruti', 'Xu', 'Jennifer']
L2= sorted(L, key=len)
print(L)
print(L2)

def get_last_name(x):
    return x[1]

#Here I am sorting them by their last names
names = [('Theresa', 'May'), ('Jo', 'Johnson'), ('Boris', 'Johnson'), ('Jeremy', 'Corbyn')] 
# list of tuples: (first_name, last_name)
print(sorted(names, key=get_last_name))

def get_last_name_first_name(x):
    return x[1], x[0]
#here I am sorting them by their last name and then their first name?
names =[('Theresa', 'May'), ('Nicola', 'Osrin'), ('Lucy', 'Ozncent'), ('Jeremy', 'Corbyn')] 
# list of tuples: (first_name, last_name)
print(sorted(names, key=get_last_name_first_name))

