# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:53:23 2019
Testing out Scikit 
@author: jose
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
#print(iris)
#print(digits)

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
