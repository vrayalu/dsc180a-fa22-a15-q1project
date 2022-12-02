import networkx as nx
import itertools

from networkx.algorithms.community import girvan_newman



class GirvanNewman:
    def __init__(self, G: nx.graph) -> None:
        self.G = G.copy()
        
    def predict(self):
        gn = girvan_newman(self.G)
        result = list(next(gn))
        
        return result
