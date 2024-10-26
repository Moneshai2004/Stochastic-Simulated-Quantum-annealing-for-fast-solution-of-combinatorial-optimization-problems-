# Quantum Annealing Project

## Overview
This project implements simulated annealing to solve the Traveling Salesman Problem (TSP) and provides a placeholder for quantum annealing. The TSP data is read from a CSV file, and simulated annealing is used to find an optimal tour.

## How to Run

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the project:
    ```bash
    python main.py
    ```

## Files

- `main.py`: Main script to run the optimization algorithm.
- `src/simulated_annealing.py`: Simulated annealing algorithm.
- `src/quantum_annealing.py`: Placeholder for quantum annealing logic.
- `src/optimization_problems.py`: Defines optimization problems (TSP, Knapsack).
- `src/utils.py`: Helper function to load data.
- `data/tsp_instance.csv`: Input data for the TSP.

## Parameters
You can modify the parameters like initial temperature, cooling rate, and max iterations in `main.py` to experiment with different settings.
