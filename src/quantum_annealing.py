import os
from dwave.system import EmbeddingComposite, DWaveSampler

def quantum_annealing(tsp_problem):
    # Set API token directly in the code (not recommended for production)
    os.environ['DWAVE_API_TOKEN'] = ''
    
    # Create Binary Quadratic Model (BQM) for the TSP
    bqm = tsp_problem.to_bqm()
    
    # Use D-Wave Sampler
    sampler = EmbeddingComposite(DWaveSampler())
    
    # Sample from the quantum annealer
    sampleset = sampler.sample(bqm, num_reads=10)
    
    # Get the best solution from the samples
    best_sample = sampleset.first.sample
    best_cost = tsp_problem.cost_function(tsp_problem.extract_solution(best_sample))
    
    return tsp_problem.extract_solution(best_sample), best_cost
