# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:36:26 2019

@author: jose
"""

l1 = [17, 'a', 2, 'tokyo']
print(len(l1))

x = [['a','b'],['c','d'],['e','f']]
print(x[2][1])
print('>>>')
for pair in x:
    print(pair[1])
    
countries = [['france', 65], ['germany', 80], ['italy', 60]]

for item in countries:
    item[1] +=1
print(countries)
print(countries[1][1])

population =[] # I created an empty list 
for item in countries: 
    population.append(item[1]) # here I add the population from each list to my 
    #my new
print(population)