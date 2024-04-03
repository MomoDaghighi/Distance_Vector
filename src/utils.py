import time
import matplotlib.pyplot as plt
import networkx as nx
from src.graph import generate_graph
from src.distance_vector import distance_vector_routing
from src.dijkstra import dijkstra_algorithm


def measure_dv_algorithm(nodes, edges):
    start_time = time.time()
    distance_vector_routing(nodes, edges)
    execution_time = time.time() - start_time
    return execution_time


def measure_dijkstra_algorithm(nodes, edges):
    start_time = time.time()
    for node in nodes:
        dijkstra_algorithm(node, nodes, edges)
    execution_time = time.time() - start_time
    return execution_time


def plot_execution_times(dv_times, dijkstra_times, node_counts):
    plt.figure(figsize=(10, 5))
    plt.plot(node_counts, dv_times, 'o-', label='Distance Vector')
    plt.plot(node_counts, dijkstra_times, 's-', label='Dijkstra')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Algorithm Execution Time Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/execution_time_comparison.png')
    plt.show()


def plot_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
