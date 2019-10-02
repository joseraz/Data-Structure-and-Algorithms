# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:10:30 2019

@author: jose
"""

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result = result + '->'
    return result
    
def DFS(graph):
    pass

def search(graph, start, end):
    pass

def testSP():
    nodes = []
    pass
