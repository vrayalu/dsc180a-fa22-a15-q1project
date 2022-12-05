import os
import requests
import networkx as nx
import pandas as pd

def get_data(is_notebook = False):
   
    url = "http://www.casos.cs.cmu.edu/computational_tools/datasets/external/polblogs/polblogs.gml"
    response = requests.get(url)

    directory = "data/"
    parent_dir = "./"
    if is_notebook:
        parent_dir = '../'
    filename = "polblogs.gml"
    path = os.path.join(parent_dir, directory)
    file_path = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(file_path):
        file = open(file_path, "wb")
        file.write(response.content)
    return file_path

def edit_graphtype(filepath):
    with open(filepath, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('directed 1', 'multigraph 1')
    with open(filepath, 'w') as file:
        file.write(filedata)
    return

def read_graph(filepath):
    G = nx.read_gml(filepath)
    nodes = pd.DataFrame.from_dict(dict(G.nodes(data=True)), orient='index')
    truth = dict(zip(nodes.index,nodes.value))
    return G, truth