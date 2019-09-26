# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:43:55 2019

@author: jose
"""

#Question for TA:
#the_35_teaser: why is it not printing the last value?
def the_35_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: integer

    Returns:
        For n divisible by 3, return '3'
        For n divisible by 5, return '5'
        For n divisible by both 3 and 5, return '35'
        Otherwise, return None.

    Example use:
    >>> the_35_teaser(9)
    '3'
    >>> the_35_teaser(95)
    '5'
    >>> the_35_teaser(300)
    '35'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if n%3 == 0 and n%5 == 0:
        return '35'
    elif n % 3 == 0:
        return '3'
    elif n % 5 == 0:
        return '5'
    else:
        return None
    
def my_looper(n):
    """
    Prints the first n values of the_35_teaser starting from 1
    
    Note you may call the function the_35_teaser
    
    Parameters:
        n: integer
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for i in range(1, n):   #can I do this in one less line? but it prints 'None'
        print(the_35_teaser(i)) #Why is this not printing the last value?
        if i == n and the_35_teaser(n) != None:
            return int(the_35_teaser(n))
        else:
            return #oh it breaks the function and stops the process
        
print(my_looper(7))
