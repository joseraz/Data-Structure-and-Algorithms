# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:12:54 2019

@author: jose
"""

def longest_item(input_list):
    """
    Finds the longest item in input_list
    
    Parameters:
        input_list: list
    Returns:
        the index of the longest item in input_list 
        (if there are ties, return the first such index)
    
    Examples:
    >>> longest_item(['hello', 'how', 'are', 'you'])
    0
    >>> longest_item('All happy families are alike'.split())
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for index, item in enumerate(input_list):
        str_len = len(input_list[index])
        location = input_list.index(input_list[index])
     return i
   
print(longest_item('All happy families are alike'.split()))
print(longest_item(['hello', 'how', 'are', 'you']))