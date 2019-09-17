# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:26:39 2019

@author: jose
"""
# square root algorithm
#x = input()
x = 10
guess = x / 2

while abs(x - guess*guess) > 0.01:
    ratio =  x / guess
    average = (ratio + guess)/2
    guess = average
print("Guess: ", guess)
print("Guess squared: ", guess*guess)

#conditional statements

rainfall = 0
if rainfall > 0.5: #condition
    # executed if condition is True
    print("Bring and Umbrella")
    
# while loop
counter = 5
while counter > 0: # condition
    #execute as long as True
    print(counter)
    counter = counter - 1
    
#making my own absolute value function
y = -1
if y > 0:
    abs_value = y 
else:
    abs_value = -y
print(abs_value)

#turning into a function
def absolute_value(y):
    if y>0:
        abs_value = y 
    else:
        abs_value = -y
    return abs_value
    
# function call
z = absolute_value(-1)
def square_root(x):
    guess = x / 2
    
    while abs(x - guess*guess) > 0.01:
        ratio =  x / guess
        average = (ratio + guess)/2
        guess = average
    return guess
    #to return more values
    #return guess, ratio, average
x = 200
print(square_root(x))
print(square_root(100))
print(square_root(500))