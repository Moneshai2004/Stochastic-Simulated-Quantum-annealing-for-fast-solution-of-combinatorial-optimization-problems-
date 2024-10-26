from dimod import BinaryQuadraticModel
import numpy as np
import random

class TSPProblem:
    def __init__(self, distance_matrix):
        # Store the distance matrix and extract the cities
        self.distance_matrix = distance_matrix
        self.cities = list(set([city for pair in distance_matrix.keys() for city in pair]))

    def initial_solution(self):
        # Create a random initial solution
        solution = self.cities[:]
        random.shuffle(solution)
        return solution

    def cost_function(self, solution):
        total_cost = 0
        # Loop through the cities in the tour
        for i in range(len(solution)):
            city1 = solution[i]
            city2 = solution[(i + 1) % len(solution)]  # Wrap around to the first city
            # Check distance for both directions
            distance = self.distance_matrix.get((city1, city2), self.distance_matrix.get((city2, city1), float('inf')))
            
            if distance == float('inf'):  # No route found
                print(f"No path between {city1} and {city2}")
                return float('inf')  # Return infinity if no valid path

            total_cost += distance
        
        return total_cost

    def get_neighbor(self, solution):
        # Generate a neighbor solution by swapping two cities
        neighbor = solution[:]
        i, j = random.sample(range(len(neighbor)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor

    def to_bqm(self):
        # Define a Binary Quadratic Model for the TSP problem
        bqm = BinaryQuadraticModel({}, {}, 0.0, 'BINARY')
        
        # Create variables and interactions based on distances
        for (city1, city2), distance in self.distance_matrix.items():
            bqm.add_variable(f'x_{city1}_{city2}', distance)
            for (city3, city4), _ in self.distance_matrix.items():
                if (city1, city2) != (city3, city4):
                    bqm.add_interaction(f'x_{city1}_{city2}', f'x_{city3}_{city4}', 1)
        
        return bqm

    def extract_solution(self, sample):
        # Extracts the TSP route based on the sample
        tour = [city for city, value in sample.items() if value == 1]
        return tour
