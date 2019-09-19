# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:04:59 2019

@author: jose
"""
answer = 0
for i in range(1,1000):
    #print('>>> inside', i)
    if i%3==0 or i%5==0:
        #print(answer, i)
        answer += i
print(answer)