import random

class Node:
    def __init__(self,city,parent,actions,total_cost,alien,civilian):
        self.city = city
        self.parent = parent
        self.actions = actions
        self.total_cost = total_cost
        self.alien = alien
        self.civilian = civilian

graph ={'A': Node('A', None, [('B',4),('C',2),('D',3)], 0, 0, 100)}