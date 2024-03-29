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

clf.fit(digits.data[:-1], digits.target[:-1])  
SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

clf.predict(digits.data[-1:])
print(array([8]))