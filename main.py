import numpy as np
import matplotlib.pyplot as plt
from src.optimization_problems import TSPProblem
from src.simulated_annealing import simulated_annealing
from src.quantum_annealing import quantum_annealing
from src.utils import load_tsp_data

# Load the TSP data
tsp_data = load_tsp_data('data/tsp_instance.csv')

# Create an instance of the TSP problem
tsp_problem = TSPProblem(tsp_data)

# Define the simulated annealing parameters
initial_temp = 1000
cooling_rate = 0.995
max_iterations = 10000
num_runs = 10

# Initialize lists for performance metrics
simulated_annealing_costs = []
quantum_annealing_costs = []

# Function to run Simulated Annealing multiple times
def run_simulated_annealing():
    best_solution, best_cost = simulated_annealing(tsp_problem, initial_temp, cooling_rate, max_iterations)
    simulated_annealing_costs.append(best_cost)
    return best_solution, best_cost

# Function to run Quantum Annealing once
def run_quantum_annealing():
    best_solution, best_cost = quantum_annealing(tsp_problem)
    quantum_annealing_costs.append(best_cost)
    return best_solution, best_cost

# Run Simulated Annealing multiple times
print("Running Simulated Annealing...")
for _ in range(num_runs):
    best_solution, best_cost = run_simulated_annealing()
    print("----------------------------------------------------")
    print("Best solution (tour):", best_solution)
    print("Best cost (total distance):", best_cost)

# Run Quantum Annealing
print("Running Quantum Annealing...")
best_solution, best_cost = run_quantum_annealing()
print("----------------------------------------------------")
print("Best solution (tour):", best_solution)
print("Best cost (total distance):", best_cost)

# Algorithm Performance Summary
print("----------------------------------------------------")
print("Algorithm Performance Summary:")
print(f"- Total runs (Simulated Annealing): {num_runs}")
print(f"- Average cost (Simulated Annealing): {sum(simulated_annealing_costs) / num_runs:.2f}")
print(f"- Average cost (Quantum Annealing): {sum(quantum_annealing_costs) / len(quantum_annealing_costs):.2f}")

# Visualization of Cost vs. Iterations
plt.plot(simulated_annealing_costs, label='Simulated Annealing Costs', marker='o')
plt.title('Cost vs. Runs for Simulated Annealing')
plt.xlabel('Run Number')
plt.ylabel('Cost')
plt.legend()
plt.grid()
plt.savefig('cost_vs_runs.png')  # Save the figure
plt.show()

# Call the visualization function for best solution from Quantum Annealing
visualize_path(best_solution, tsp_problem.distance_matrix)

# Conclusion
print("Conclusion: Simulated Annealing provided a best cost of", min(simulated_annealing_costs))
print("Quantum Annealing provided a best cost of", best_cost)
print("Future Work: Explore further optimizations in both algorithms.")
