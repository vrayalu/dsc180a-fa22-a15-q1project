import networkx as nx
import itertools

from networkx.algorithms.community import louvain_communities



class Louvain:
    def __init__(self, G: nx.graph) -> None:
        self.G = G.copy()
        
    def predict(self):
        return louvain_communities(self.G)