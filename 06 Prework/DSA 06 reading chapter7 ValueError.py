# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:52:37 2019

@author: jose
"""
#it does not like the raw_input function
val = int((input('Enter an integer: '))

while val == 1:
    val = input('Enter a digit: ')
    try:
        val = int(val)
        print('The square of the number you entered is', val**2)
        break #to exit the while loop
    except ValueError:
        print(val, 'is not an integer')