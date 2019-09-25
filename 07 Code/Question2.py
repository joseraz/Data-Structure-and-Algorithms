# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:43:19 2019
Pocket Monsters!
@author: jose
"""

class Monster(object):
    def __init__(self, name, monster_type, combat_points, hit_points):
        self.name = name
        self.monster_type = monster_type
        self.combat_points = combat_points # strength in combat
        self.hit_points = hit_points # max health
        self.health = hit_points # current health
    
    def print_monster(self):
        print('A monster called {}.'.format(self.name))
    
    def get_health(self):
        return self.health
    
    def get_hit_points(self):
        return self.hit_points
    
    def print_health_status(self):
        if self.health <= 0:
            print('{} is knocked out!'.format(self.name))
        else: print('{0} has {1} health left.'.format(self.name, self.health))
    
    def hurt(self, damage):
        """
        Reduce monster health by damage to a minimum of zero
        """
        self.health = max(self.health - damage, 0)
        print('{} is hurt!'.format(self.name))
        self.print_health_status()
    
    def __str__(self):
        print('>>> Testing a string')
        return self.name

              
pika = Monster('Pikachu', 'electric', 100, 80)
pika.hurt(10)