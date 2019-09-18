# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:28:55 2019

@author: jose
"""

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print(t1 + t2)
print('>>>')
print((t1 + t2)) # same with both parentesis
# wait no, I think double parenthesis is the tuple interpreted as a int
print((t1 + t2)[3]) 
print((t1 + t2)[2:5])   

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples. 
    Returns a tuple containing elements that are in both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result