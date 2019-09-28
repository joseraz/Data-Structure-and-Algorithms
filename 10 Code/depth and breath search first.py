# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:23:55 2019

@author: jose
"""

class Node: #This makes a object class called Node
    def __init__(self, value): #Calls init function and one value
        self.value = value #assigns the value to the self
        self.adjacentNodes = [] #assigns a list of adjancentNodes to the self with an empty list
        
def depthFirst(node, soughtValue): #This tells the node to llos for a value
    if node.value == soughtValue:   #This is when it finds the node to return True
        return True
    for adjNode in node.adjacentNodes: # A recursion to call again the function and keep searching
        depthFirst(adjNode, soughtValue)  # Inception style you have to go deeper
        