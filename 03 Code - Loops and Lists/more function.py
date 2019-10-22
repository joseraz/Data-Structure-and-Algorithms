# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:23:50 2019

@author: jose
"""

def create_list_squares(n):
    num_list = []
    for number in range(n):
        num_list.append(number*number)
    return num_list
        
def create_list_cubes(n):
    num_list = []
    for number in range(n):
        num_list.append(number*number*number)
    return num_list

def create_list_calc(n, func):
    num_list = []
    for number in range(n):
        num_list.append(func(number))
    return num_list

def square(x):
    return x*x

square_list = create_list_calc(5, square)
print(square_list)

def power_creator(n):
    def f(x):
        return x**n
    return f

square = power_creator(2)
print(square(5))
cube = power_creator(3)
print(cube(2))