# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:04:52 2019

@author: jose
"""

d ={'dog':'bone', 'cat':'mouse'}
print('mouse' in d)

print('>>>')
x = [2,3,1]
x = x + x
print(x[2]*x[0]-x[3])

points = {'Maria': [4,2], 'Tome': [1,4]}
total = []
for i in points:
    total.append(sum(points[i]))
print(total)

a = [3,6,8,2]
b = ['a', 'A', 'er']
c = a[3::-2] + b[:-1]
c