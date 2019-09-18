# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:39:29 2019

@author: jose
"""

def isPalindrome(s):
    """Assumes s is a str
       Returns True if letters in s form a palindrome; False otherwise
       Non-letter and capitalization are ignored."""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': #what does this mean???
                   letters = letters + c
        return letters
        
    def isPal(s):
           if len(s) <= 1:
               return True
           else:
               return s[0] == s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))

def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))