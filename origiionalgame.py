from collections import deque
import random

class Node:
    def __init__(self,city,parent,actions,total_cost,alien,civilian):
        self.city = city
        self.parent = parent
        self.actions = actions
        self.total_cost = total_cost
        self.alien = alien
        self.civilian = civilian

def spawn_aliens_bfs(graph, source):
    
    frontier = deque([source])
    visited_nodes = set()
    all_paths = []


    while frontier:
        current_node = frontier.popleft()

        #randomly generate aliens in each city 
        current_node.alien = random.randint(100, 500)

        print(f"Node: {current_node.city}, Random Aliens spawned: {current_node.alien}")

        visited_nodes.add(current_node.city)

        #print(f"Visited: {visited_nodes}")

        for action in current_node.actions:
            child = Node(action[0], current_node, graph[action[0]].actions, graph[action[0]].total_cost, graph[action[0]].alien, graph[action[0]].civilian)

            if child.city not in visited_nodes and not any(n.city == child.city for n in frontier):
                #print(child.city)
                
                frontier.append(child)
                #print(f"Frontier: {[n.city for n in frontier]}")
                
   
    return all_paths


graph ={'A': Node('A', None, [('B',4),('C',2),('D',3)], 0, 0, 100),
        'B': Node('B', None, [('E',5),('A',4)], 0, 0, 300),
        'C': Node('C', None, [('A',2),('D',1),('Alexendria',5)], 0, 0, 600),
        'D': Node('D', None, [('A',3),('C',1)], 0, 0, 100),
        'E': Node('E', None, [('B',5),('F',7)], 0, 0, 50),
        'F': Node('F', None, [('E',7),('G',2)], 0, 0, 800),
        'G': Node('G', None, [('Alexendria',2),('F',2)], 0, 0, 700),
        'Alexendria': Node('Alexendria', None, [('C',5),('G',2)], 0, 0, 400)}

source_node = Node(graph['A'].city, None, graph['A'].actions, 0, 0, 0)

spawn_aliens_bfs(graph,source_node)

