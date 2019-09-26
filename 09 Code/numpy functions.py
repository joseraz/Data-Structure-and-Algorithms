# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:44:17 2019

@author: jose
"""
import numpy as np
import array

list(range(10,20,2))

L = list(range(10))
L
type(L[0])

L2 = [str(c) for c in L]
L2
type(L2[0])

L3 = [True, "2", 3.0, 4]
[type(item) for item in L3]

L = list(range(10))
A = array.array('i',L)
A

a = np.array([1,4,2,5,3])

b = np.array([1,4,2,5,3], dtype='float32')

c = np.array([range(i,i+3) for i in [2, 4, 6]])
c

d = np.zeros(10, dtype=int)
d

e = np.ones((3,5), dtype=float)
e

f= np.full((4,4), 3.14)
f

g = np.arange(0,20,2)
g

h = np.linspace(0,2,12)
h

i = np.random.random((3,3)) # For values between zero and 1
i

j = np.random.normal(0, 1, (3,3))
j

k = np.random.randint(0,10, (3,3))
k

np.eye(4)

np.empty(3)