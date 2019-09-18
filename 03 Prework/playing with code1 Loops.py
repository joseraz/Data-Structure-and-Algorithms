# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:14:10 2019

@author: jose
"""
# ahhh, I get it now, so it takes the value of x and uses it for the first
#iteration of each cycle
x = 3
for j in range(x):
    print (">>> 1st loop >>>")
    #x=4
    for i in range(x):
        print (">>> 2Loop")
        print(i)
        x = 4
        