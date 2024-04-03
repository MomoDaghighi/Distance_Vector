import numpy as np


# Initialize the distance table for all nodes
def initialize_distance_vector(nodes, edges):
    distance_table = {node: {n: np.inf for n in nodes} for node in nodes}
    next_hop = {node: {n: None for n in nodes} for node in nodes}
    for node in nodes:
        distance_table[node][node] = 0
    for (n1, n2, cost) in edges:
        distance_table[n1][n2] = cost
        distance_table[n2][n1] = cost
        next_hop[n1][n2] = n2
        next_hop[n2][n1] = n1
    return distance_table, next_hop


# Update the distance table using the Bellman-Ford equation
def update_distance_vector(node, nodes, distance_table, next_hop):
    updated = False
    for neighbor in next_hop[node].values():
        if neighbor is not None:
            for n in nodes:
                if distance_table[node][n] > distance_table[node][neighbor] + distance_table[neighbor][n]:
                    distance_table[node][n] = distance_table[node][neighbor] + distance_table[neighbor][n]
                    next_hop[node][n] = neighbor
                    updated = True
    return updated


# The main function that performs the Distance Vector routing
def distance_vector_routing(nodes, edges):
    distance_table, next_hop = initialize_distance_vector(nodes, edges)
    while True:
        changes = []
        for node in nodes:
            changed = update_distance_vector(node, nodes, distance_table, next_hop)
            changes.append(changed)
        if not any(changes):
            break
    return distance_table


def display_final_cost_tables(distance_table):
    print("Final Cost Tables:")
    for node, table in distance_table.items():
        print(f"Node {node} costs to other nodes:")
        for destination, cost in table.items():
            print(f"  to node {destination}: cost {cost}")
        print()
