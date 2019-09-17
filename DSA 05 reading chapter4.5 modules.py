# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:12:59 2019

@author: jose
"""

import circle

pi = 3.0 # does not change anything, the value of the module circle.py is different

# use reload to reimport the module, can cause lots of bugs if you changed stuff

print(circle.pi)
print(circle.area(3))