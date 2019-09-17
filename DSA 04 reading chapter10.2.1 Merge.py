# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:24:59 2019

@author: jose
"""

def merge(left, right, compare):
    """Assumes left and right are assorted lists and 
    compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the same elements as (left + right)
    would contain"""
    
    result = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

#import operator
            