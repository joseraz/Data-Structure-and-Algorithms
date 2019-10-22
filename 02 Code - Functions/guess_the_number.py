# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:28:02 2019

@author: jose
"""
import random

def guess_the_number(min_value, max_value):
    """
    User must guess the value of a number between min_value and max_value

    Parameters:
        min_value, max_value (integers)
    """
    x = random.randint(min_value, max_value)
    print(f">>> A number has been picked between {min_value} and {max_value}.")
    print(f">>> Can you guess the number?")
    i = int(input('>>> ') )
    while i != x:
        if i > x:
            print("Too high!")
            i = int(input('>>> ') )
        else:
            print("Too low!")
            i = int(input('>>> ') )
    return 'Congrats! you got it!' #what is the benefit of using return rather than print?