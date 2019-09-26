# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:33:59 2019

@author: jose
"""

def max(a,b):
    if a >b :
        return a
    else:
        return b

def palindrome(str,k1):
    l=0
    r=len(str)-1
    pl=str
    k=int(k1)
    while (l < r):
        if str[l] != str[r] :
            pl[l]=pl[r]=max(str[l],str[r])
            l+=1
            r-=1
        if k<= 0:
           return "can not able to make palin "
    l=0
    r=len(str)-1
    while l<= r:
        if l == r:
                if k>0:
                    pl[l]='9'
        if pl[l] < '9':
            if k>=2 and str[l]==pl[l] and str[r]==pl[r]:
                k-=2
                pl[l]=pl[r]='9'

        elif k>=1 and (str[l]!=pl[l] or str[r]!=pl[r]):
            k-=1
            pl[l]=pl[r]='9'
        l+=1
        r-=1
    return pl

print(palindrome(list["11119111"], 4))