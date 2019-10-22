# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:18:49 2019

@author: jose
"""

some_list = [3,6,4,8,'joe',875,'76'] 

index = 0
for item in some_list:
    print('The value is:',item,', the index is:',index)
    index += 1
    

print('>>> The pythonic way')
#Python provides us with the built-in function enumerate(), 
#which returns the index along with the value of the cell:
for index, item in enumerate(some_list):
    print('The vale of index is: ', index, 'and the item is: ', item)

# In many cases we need to loop through two lists at the same time. 
# Instead of using the same index for two different lists, 
#this can be done using the built in function zip( ):
names = ['Mary', 'Nick', 'John', 'Sue'] 
grades = [87, 45, 75, 91] 

for name, grade in zip(names, grades): 
    print(name, ' got ', grade)