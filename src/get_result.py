import sys
sys.path.append('..')

import numpy as np
import networkx as nx
import pandas as pd

from collections import defaultdict
from src.models import weighted_threshold



def calculate_accuracy(predictions: list, actual: dict) -> float:
    purities = []
    for community in predictions:
        label_count = defaultdict(int)
        max_count = 0
        
        for node in community:
            label = actual[node]
            label_count[label] += 1
            max_count = max(max_count, label_count[label])
            
        purities.append(max_count)
        
    return np.sum(purities) / len(actual)

def train_weighted(data):
    weighted_threshold_predictions = weighted_threshold.WeightedThresholdCommunity(data).predict()
    return weighted_threshold_predictions

def get_result(data: nx.graph, ground_truth: dict):
    results = dict()
    
    
    results["weighted_threshold"] = calculate_accuracy(weighted_threshold_predictions, ground_truth)
    
    output = pd.DataFrame({"Accuracy": results})
    
    return output