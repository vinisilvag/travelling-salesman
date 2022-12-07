import numpy as np
import networkx as nx
from queue import PriorityQueue

from math import ceil

import sys

def initial_bound(weights, no_nodes):
    total = 0

    sorted_weights = weights.copy()
    sorted_weights.sort(axis=1)

    for i in range(no_nodes):
        total += sorted_weights[i][1]
        total += sorted_weights[i][2]

    return ceil(total / 2)
    total = 0
    no_nodes = weights.shape[0]

def bnb_tsp(weights, graph):
    no_nodes = graph.number_of_nodes()

    root = (initial_bound(weights, no_nodes), 0, 0, [0]) # bound, level, cost, solution
    queue = PriorityQueue()
    best = sys.maxsize # infinity
    solution = [] # vertices order

    queue.put(root)

    while not queue.empty():
        partial_bound, level, cost, partial_solution = queue.get()

        if level > no_nodes:
            if best > cost:
                best = cost
                solution = partial_solution
        elif partial_bound < best:
            connect_to_source = weights[partial_solution[-1][0]]
            best_bound = bound(weights, partial_solution.copy().append(0), no_nodes)

            if node.level < no_nodes:
                for k in range(no_nodes):
                    distance = weights[partial_solution[-1]][k]
                    bound_value = bound(weights, partial_solution.copy().append(k), no_nodes)

                    if k not in partial_solution and distance != 0 and bound_value < best:
                        new_node = (bound_value,
                                    level + 1,
                                    cost + distance,
                                    partial_solution.copy().append(k))
                        queue.put(new_node)

            elif connect_to_source != 0 and best_bound < best and len(node.solution) == no_nodes:
                possible_solution = (best_bound,
                                     level + 1,
                                     cost + connect_to_source,
                                     partial_solution.copy().append(0))
                queue.put(possible_solution)

    return solution, best
