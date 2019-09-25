# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:20:51 2019
Data Structure Class 01
@author: jose
"""
"""
a = 5
b = 6
temp = a 
a = b
b = temp
print(a)
print(b)

x = 'Franz'
y = 'Kafka'
z = x+y
print(z)

print('Two'*1 + 'Three'*2)
phrase = 'It wasn\'t me'
print('It wasn\'t me')

first_name = 'Franz'
last_name = 'Kafka'
book_name = 'The Trial'
book_year = 1925
text = (first_name + ' ' + last_name + ' published ' + book_name + ' in ' + str(book_year))
print(text)

price1 = 400000
price2 = 500000
price_change = (price2 - price1) / price1 * 100
print(price_change)

#print(0>=0 and 0 and True)
print(5*4 ==20, 5>=5, not 5 != 4)
"""
# Define a variable called age and assign it the value 19 (or a different integer)
# Write a condition that prints out the string 'You're old enough to vote.' if age is greater than or equal to 18.
# Otherwise, the condition prints out 'Sorry, you still have to wait out x years before you can vote.',
# where x is the difference between 18 and age
# You'll need to use at least an if-structure, a type conversion, and the print function.
age = 13
if age >= 18:
    print('You\'re old enough to vote.')
else:
    x = 18 - age
    print(f"Sorry, you still have to wait out {x} years before you can vote.")