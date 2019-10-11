# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:16:41 2019

@author: jose
"""

#If 2520 is divisible by 1 to 10, then I need the numbers from 11 to 20
"""x=2520
prime = [11, 13, 17, 19]
for i in prime:
    x *=i
    print(x, i)

print(x)"""
def myAttemp():
    y = 13195
    n = 1
    div = []
    while n<y/2:
        if y%n == 0:
            div.append(n)
            #print(n)
        n += 1
    print(div)

def stackOverflow(n):
    i = 2
    while i * i < n:
        print('Outer loop', n, ' number', i)
        while n%i == 0:
            n = n / i
            print('In Loop:', n, 'primer number', i)
        i = i + 1
    print(n)
    
stackOverflow(13195)
#stackOverflow(600851475143)