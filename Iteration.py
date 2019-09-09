# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:08:10 2019

@author: jose
"""

x = 3 
ans = 0
itersLeft = 3
while(itersLeft != 0):
    ans += x
    itersLeft = itersLeft -1
print( str(x) + '*' + str(x) + ' = ' + str(ans))

"""
max = int(input('Enter a positive Integer: '))
i = 0
while i < max:
    i += 1
print(i)
"""
x = 25
epsilon = 0.01
numGuess = 0
low = 0
high = 25
ans = (high + low)/2.0 
while abs(ans**2 -x ) >= epsilon:
    print(('low = '), low, ('high = '), high, ('ans = '), ans)
    numGuess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans 
    ans = ( high + low )/2.0
print('numGuess = ', numGuess)
print( ans, 'is close to square root of', x)