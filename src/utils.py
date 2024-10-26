import pandas as pd

def load_tsp_data(file_path):
    df = pd.read_csv(file_path)
    distance_matrix = {}
    
    # Create a distance dictionary
    for _, row in df.iterrows():
        city1, city2, distance = row['City1'], row['City2'], row['Distance']
        distance_matrix[(city1, city2)] = distance
        distance_matrix[(city2, city1)] = distance  # Ensure it's bidirectional
    
    return distance_matrix
