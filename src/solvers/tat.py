import numpy as np
import networkx as nx

def tat_tsp(graph):
    best = 0

    mst = nx.minimum_spanning_tree(graph)

    path = list(nx.dfs_preorder_nodes(mst, source=0))
    path.append(path[0])

    for i in range(len(path) - 1):
        best += graph[path[i]][path[i + 1]]['weight']

    return path, best
