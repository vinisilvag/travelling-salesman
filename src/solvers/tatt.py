import numpy as np
import networkx as nx

import sys

def tatt_tsp(graph, cost):
    mst = nx.minimum_spanning_tree(graph)
    solution = list(nx.dfs_preorder_nodes(mst))

    return solution, sys.maxsize
