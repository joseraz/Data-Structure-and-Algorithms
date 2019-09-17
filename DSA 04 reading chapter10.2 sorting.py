# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:50:15 2019

@author: jose
"""

def selSort(L):
    """Assumes that L is a list of elements that can be compared using >.
    Sorts L in ascending order."""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element of suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap positions of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart +=1
        