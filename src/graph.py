import numpy as np


def generate_graph(num_nodes, edges):
    nodes = range(num_nodes)
    return nodes, edges


def generate_random_graph(num_nodes, edges):
    nodes = range(num_nodes)
    if not edges:  # If no edges provided, generate random edges
        for i in nodes:
            for j in range(i + 1, num_nodes):
                if np.random.rand() > 0.5:
                    cost = np.random.randint(1, 10)
                    edges.append((i, j, cost))
    return nodes, edges