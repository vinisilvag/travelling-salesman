import numpy as np
import networkx as nx
from queue import PriorityQueue

from math import ceil

import sys

def bound(weights, solution, no_nodes):
    selected = {} # dictionary with the nodes in the graph

    for i in range(no_nodes):
        selected[i] = {} # create dictionary with all nodes in the graph

    copy = weights.copy()
    copy.astype(int)

    for i in range(len(solution) - 1): # insert the fixed edges by the partial solution
        start = solution[i]
        end = solution[i + 1]

        selected[start].update({ end: copy[start][end] })
        selected[end].update({ start: copy[end][start] })

        copy[start][end] = sys.maxsize

    # insert edges in each node with less than 2 fixed edges by the partial solution
    for key in selected:
        if len(selected[key].keys()) == 2: continue

        while len(selected[key].keys()) < 2:
            minimal = sys.maxsize
            minial_idx = -1

            for i, w in enumerate(copy[key]):
                if w == 0: continue

                if w < minimal:
                    minimal = w
                    minimal_idx = i

            selected[key].update({ minimal_idx: minimal })

            copy[key][minimal_idx] = sys.maxsize

    total = 0

    # sum edges
    for start in selected:
        for end in selected[start]:
            total += selected[start][end]

    # calculate the metric
    return ceil(total / 2)

def bnb_tsp(weights, graph):
    no_nodes = graph.number_of_nodes() # number of nodes

    root = (bound(weights, [0], no_nodes), 0, 0, [0]) # bound, level, cost, solution
    queue = PriorityQueue()
    best = sys.maxsize # infinity
    solution = [] # vertices order

    queue.put(root)

    while not queue.empty():
        partial_bound, level, cost, partial_solution = queue.get()

        if level + 1 > no_nodes:
            if best > cost:
                best = cost
                solution = partial_solution

        elif partial_bound < best:
            if level + 1 < no_nodes:
                for k in range(1, no_nodes):
                    if k not in partial_solution:
                        distance = weights[partial_solution[-1]][k]

                        incremented_solution = partial_solution.copy()
                        incremented_solution.append(k)

                        bound_value = bound(weights, incremented_solution, no_nodes)

                        if distance != 0 and bound_value < best:
                            queue.put((bound_value, level + 1, cost + distance, incremented_solution))
            else:
                connect_to_source = weights[partial_solution[-1]][0]

                if connect_to_source != 0:
                    solution_connect_source = partial_solution.copy()
                    solution_connect_source.append(0)
                    best_bound = bound(weights, solution_connect_source, no_nodes)

                    if best_bound < best and len(partial_solution) == no_nodes:
                        queue.put((best_bound, level + 1, cost + connect_to_source, solution_connect_source))

    return solution, best
