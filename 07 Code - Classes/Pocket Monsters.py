# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:42:14 2019

@author: jose
"""

class Monster(object):
    """
    Pocket Monsters
    """
    # Double underscore init double underscore
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def say_hello(self):
    # Self refers to specific instance
    # making the function call
            print(f"Hi, my name is {self.name}")
            
    def hurt(self, damage):
        self.health = self.health - damage
        print(f"{self.name} has {self.health} health left.")
        if self.health <= 0:
            print(f"{self.name} is dead!")
        
                
# Create nuew instance of monster
# this calls __init__ function
pikachu = Monster("Pikachu",100)
# Name Attribute
pikachu.name
# Equivalent
pikachu.say_hello() # Thi is what python does Monster.say_hello(pikachu)
Monster.say_hello(pikachu)

# Same idiom as:
L = list ()
L.append(1)

squirtle = Monster("Squirtle", 80)
pikachu.hurt(35)
pikachu.hurt(35)
pikachu.hurt(35)

# Careful 
pikachu.name == "Pikachu"

pikachu.get_name() == "Pikachu"
# Impossible to make the same error
#pikachu.get_name() = "Pikachu"
