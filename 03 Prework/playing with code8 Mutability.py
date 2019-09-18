# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 07:25:09 2019

@author: jose
"""

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Unis = [Techs, Ivys]
Universities = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print(Unis == Universities)
# where does it check the components?

print(id(Unis) == id(Universities))
print(id(Unis))
print(id(Universities))
# what is that id value that is being stored?