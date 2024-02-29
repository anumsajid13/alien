import random

class Node:
    def __init__(self,city,parent,actions,total_cost,alien,civilian):
        self.city = city
        self.parent = parent
        self.actions = actions
        self.total_cost = total_cost
        self.alien = alien
        self.civilian = civilian

graph ={'A': Node('A', None, [('B',4),('C',2),('D',3)], 0, 0, 100),
        'B': Node('B', None, [('E',5),('A',4)], 0, 0, 300),
        'C': Node('C', None, [('A',2),('D',1),('Alexendria',5)], 0, 0, 600),
        'D': Node('D', None, [('A',3),('C',1)], 0, 0, 100),
        'E': Node('E', None, [('B',5),('F',7)], 0, 0, 50),
        'F': Node('F', None, [('E',7),('G',2)], 0, 0, 800),
        'G': Node('G', None, [('Alexendria',2),('F',2)], 0, 0, 700),
        'Alexendria': Node('Alexendria', None, [('C',5),('G',2)], 0, 0, 400)}