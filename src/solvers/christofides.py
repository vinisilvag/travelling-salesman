import numpy as np
import networkx as nx

def christofides_tsp(graph):
    best = 0
    path = []

    mst = nx.minimum_spanning_tree(graph)

    odd_nodes = []
    degrees = nx.degree(graph)

    for item in degrees:
        node, degree = item

        if degree % 2 != 0:
            odd_nodes.append(node)

    odd_degree_subgraph = nx.subgraph(graph.copy(), odd_nodes)
    edges = list(nx.min_weight_matching(odd_degree_subgraph))

    multigraph = nx.MultiGraph()

    for i, j, weight in graph.edges(data=True):
        multigraph.add_edge(i, j, weight=weight)

    for edge in edges:
        i, j = edge
        multigraph.add_edge(i, j, weight=odd_degree_subgraph[i][j])

    # TODO: compute eulerian path (dfs?)

    for i in range(len(path) - 1):
        best += graph[path[i]][path[i + 1]]['weight']

    return path, best
