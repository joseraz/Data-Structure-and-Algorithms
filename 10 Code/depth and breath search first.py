# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:23:55 2019

@author: jose
"""

class Node: #This makes a object class called Node
    def __init__(self, value): #Calls init function and one value
        self.value = value #assigns the value to the self
        self.adjacentNodes = [] #assigns a list of adjancentNodes to the self with an empty list
        
def depthFirst(node, soughtValue, visitedNodes): #This tells the node to look for a value
    if node.value == soughtValue:   #This is when it finds the node to return True
        return True
    
    visitedNodes.add(node) #Added this to keep track of visited nodes
    for adjNode in node.adjacentNodes: # A recursion to call again the function and keep searching
        if adjNode not in visitedNodes: #Thi is to avoid the algorithm from looping infinitely
            if depthFirst(adjNode, soughtValue, visitedNodes):
                return True    # Inception style you have to go deeper
            
    return False

from collection import queue

def depthFirst2(startingNode, soughtValue):
    visitedNodes = set()
    queue = deque([StartingNode])
    
        