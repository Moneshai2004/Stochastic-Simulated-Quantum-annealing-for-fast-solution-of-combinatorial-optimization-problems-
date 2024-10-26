# src/simulated_annealing.py

import numpy as np
import random

def simulated_annealing(problem, initial_temp, cooling_rate, max_iterations):
    # Initialize
    current_solution = problem.initial_solution()
    best_solution = current_solution
    current_cost = problem.cost_function(current_solution)
    best_cost = current_cost
    temperature = initial_temp

    for _ in range(max_iterations):
        new_solution = problem.get_neighbor(current_solution)
        new_cost = problem.cost_function(new_solution)

        # Accept new solution based on probability
        if new_cost < current_cost or np.exp((current_cost - new_cost) / temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost

        # Update the best solution found
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, best_cost
