import heapq
import numpy as np


def dijkstra_algorithm(start_node, nodes, edges):
    shortest_paths = {node: np.inf for node in nodes}
    shortest_paths[start_node] = 0
    priority_queue = [(0, start_node)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_node]:
            continue
        for (n1, n2, cost) in edges:
            if n1 == current_node or n2 == current_node:
                neighbor = n2 if n1 == current_node else n1
                distance = current_distance + cost
                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths
