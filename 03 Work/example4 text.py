# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:57:09 2019

@author: jose
"""

test_word = 'abcdef'
print(test_word[1:5])
print(test_word[:-1])
print(test_word[5:1:-2])
print(test_word[::-1])
print(test_word[0]) #= 'w'
print('>>>')
vowels = 'aeiouy'

for letter in vowels:
    print(letter) 
    
sentence = 'The Python language was created by Guido van Rossum. It was named after Monty Python.'
sent_list = sentence.split() # this separate every world inside the sentence
sent_list = sentence.split()
print(sent_list)
sent_list = sentence.split('.') #this separates the sentences by a dot
sent_list = sentence.split('.')
print(sent_list)