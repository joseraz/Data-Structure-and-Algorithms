# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:08:56 2019

@author: jose
"""

german_cities = ['Berlin', 'Munich', 'Frankfurt'] 
print(f'We visited {german_cities[1]} first.')

#help(str.split)

word = 'hElLo!'

print(((word.lower().capitalize()))) # which is first? lower or capitalize?

word = 'lovely day'
count = 0 
for letter in word:
    print('>>> inside')
    print(count)
    if letter in 'hey': #the if staments stops this at three
        print('>>> inside if')
        count += 1
        print(count)
print(count) #it compares with e and y against word and does it every time they match

    
