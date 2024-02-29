import networkx as nx
import random

class AlienInvasionGame:
    def __init__(self, num_cities, num_bases, distances):
        self.graph = self.generate_graph(num_cities, num_bases, distances)
        self.aliens_spawned = {}
        self.weapons_used = {}
        self.civilians_saved = {}

    def generate_graph(self, num_cities, num_bases, distances):
        graph = nx.Graph()
        cities = [f"City_{i}" for i in range(num_cities)]
        bases = random.sample(cities, num_bases)

        cities.append("Alexandria")
        for city in cities:
            graph.add_node(city)
            for base in bases:
                if city != base:
                    distance = distances.get((city, base), distances.get((base, city), 1))
                    graph.add_edge(city, base, distance=distance)

        return graph

    def initialize_game(self, start_node, destination_node):
        self.aliens_spawned = {node: random.randint(100, 1000) for node in self.graph.nodes}
        self.weapons_used = {node: 0 for node in self.graph.nodes}
        self.civilians_saved = {node: 0 for node in self.graph.nodes}

        self.run_bfs(start_node, destination_node)

    def run_bfs(self, start_node, destination_node):
        path = nx.shortest_path(self.graph, source=start_node, target=destination_node)
        for i in range(len(path) - 1):
            current_city, next_city = path[i], path[i + 1]
            alien_quota = self.aliens_spawned[next_city]
            civilians = random.randint(50, 200)
            weapons_needed = self.calculate_weapons_needed(alien_quota, civilians)
            
            # Update game state
            self.weapons_used[current_city] += weapons_needed
            self.civilians_saved[next_city] += civilians

            print(f"Saved {civilians} civilians in {next_city} using {weapons_needed} weapons.")

    def calculate_weapons_needed(self, alien_population, civilian_population):
        # Your heuristic function here
        # Use factors like military bases, weapons, civilians, aliens, distances, etc.
        # Example heuristic: weapons_needed = alien_population // 2 + civilian_population // 3
        return alien_population // 2 + civilian_population // 3

# Example usage
num_cities = 5
num_bases = 2
distances = {("City_0", "City_1"): 3, ("City_1", "City_2"): 4, ("City_2", "City_3"): 2, ("City_3", "City_4"): 5}
start_node = "City_0"
destination_node = "Alexandria"

game = AlienInvasionGame(num_cities, num_bases, distances)
game.initialize_game("City_0", "Alexandria")