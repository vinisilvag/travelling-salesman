import numpy as np
from queue import PriorityQueue
import sys

def bnb_tsp(graph, n):
    # root = (...)
    queue = PriorityQueue()
    best = sys.maxsize
    solution = []

    # queue.put(root)

    while not queue.empty():
        node = queue.get()

        if node.level > n:
            if best > node.cost:
                best = node.cost
                solution = node.solution
        elif node.bound < best:
            if node.level < n:
                for idx in enumerate(n):

def main():
    # gen entrie
    # create graph
    # call bnb-tsp

if __name__ == "__main__":
    main()
