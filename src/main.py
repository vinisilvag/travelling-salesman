import numpy as np
import networkx as nx

from solvers.bnb import bnb_tsp
from solvers.tatt import tatt_tsp

def main():
    no_instances = 1 # number of instances
    instances_path = '../experiments/instances' # instances path
    output_path = '../experiments/output.csv' # output path

    output = open(output_path, 'w')

    output.write('method,entrie,metric,solution,path_cost\n')

    for k in range(no_instances):
        # load weights matrix
        weights = np.loadtxt(f'{instances_path}/entrie{k}.txt',
                             dtype=np.int16)

        # create and populate graph
        graph = nx.Graph()

        for i, line in enumerate(weights):
            for j, weight in enumerate(line):
                if weight == -1: continue

                graph.add_edge(i, j, weight=weight)

        no_nodes = len(graph) # number of nodes

        # call bnb solver for tsp
        bnb_sol, bnb_best = bnb_tsp(graph, no_nodes)
        print('bnb:', bnb_sol)

        output.write(f'branch-and-bound,entrie{k}.txt,euclidean,solution,path_cost\n')
        output.write(f'branch-and-bound,entrie{k}.txt,manhattan,solution,path_cost\n')

        tatt_sol, tatt_cost = tatt_tsp(graph, 0)
        print('tatt:', tatt_sol)
        # TODO: write reuslt in ../experiments/output.txt file

        # TODO: call christofides solver
        # TODO: write result in ../experiments/output.txt file

if __name__ == '__main__':
    main()
