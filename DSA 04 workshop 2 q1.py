# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:25:43 2019

@author: jose
"""

def Lsum(L):
    #L is a list with at least two items
    list_sum = L[0]
    for item in L[1:]:
        list_sum = list_sum + item
    print(list_sum)

x = Lsum([2, 2, 1])
print(x)