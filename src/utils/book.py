# example of the book (to verify if the algorithms implemented are correct)
import os
import sys

util_dir = os.path.dirname(__file__)
solvers = os.path.join(util_dir, '..')
sys.path.append(solvers)

import numpy as np
import networkx as nx

from solvers.tat import tat_tsp
from solvers.christofides import christofides_tsp
from solvers.bnb import bnb_tsp

entrie = np.array([[ 0, 4,  8,  9, 12],
                   [ 4, 0,  6,  8,  9],
                   [ 8, 6,  0, 10, 11],
                   [ 9, 8, 10,  0,  7],
                   [12, 9, 11,  7,  0]])

e_bnb = np.array([[0, 3, 1, 5, 8],
                [3, 0, 6, 7, 9],
                [1, 6, 0, 4, 2],
                [5, 7, 4, 0, 3],
                [8, 9, 2, 3, 0]])

bnb_graph = nx.from_numpy_matrix(entrie, create_using=nx.Graph())

sol, cost = bnb_tsp(e_bnb, bnb_graph)

print(sol)
print(cost)

#graph = nx.from_numpy_matrix(entrie, create_using=nx.Graph())

#tat_sol, tat_cost = tat_tsp(graph)
#print("TAT:")
#print("Path",tat_sol)
#print("Cost:", tat_cost)

#ch_sol, ch_cost = christofides_tsp(graph)
#print("CHRISTOFIDES:")
#print("Path:", ch_sol)
#print("Cost:", ch_cost)
