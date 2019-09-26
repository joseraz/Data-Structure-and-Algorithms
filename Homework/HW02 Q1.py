# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:25:02 2019

@author: jose
"""

def moving_average(l, N):
    sum = 0
    result = list( 0 for x in l)

    for i in range( 0, N ): #this is for the first intengers
        sum = sum + l[i]
        result[i] = sum / (i+1)

    for i in range( N, len(l) ):
        sum = sum - l[i-N] + l[i]
        result[i] = sum / N

    return result

print(moving_average([2,3,4,5,8,5,4,3,2,1], 2))