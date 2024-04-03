from src.distance_vector import distance_vector_routing, display_final_cost_tables
from src.graph import generate_graph, generate_random_graph
from src.utils import measure_dv_algorithm, measure_dijkstra_algorithm, plot_graph, plot_execution_times


def main():
    while True:
        try:
            num_nodes = int(input("Enter the number of nodes: "))
            if num_nodes <= 0:
                raise ValueError("Number of nodes must be a positive integer.")
            break
        except ValueError as e:
            print("Invalid input:", e)

    edges = []
    print("Enter the edges in the format 'node1 node2 cost' (without quotes), enter 'done' when finished:")

    while True:
        edge_input = input()
        if edge_input.lower() == 'done':
            break
        try:
            parts = edge_input.split()
            if len(parts) != 3:
                raise ValueError("Each edge input must contain exactly three values.")

            node1, node2, cost = map(int, parts)
            if not (0 <= node1 < num_nodes) or not (0 <= node2 < num_nodes):
                raise ValueError("Node numbers must be between 0 and", num_nodes - 1)
            if cost <= 0:
                raise ValueError("Cost must be a positive integer.")

            edges.append((node1, node2, cost))
        except ValueError as e:
            print("Invalid input:", e)

    nodes, edges = generate_graph(num_nodes, edges)

    # Plot the graph
    plot_graph(nodes, edges)

    # Display final cost tables
    final_distance_table = distance_vector_routing(nodes, edges)
    display_final_cost_tables(final_distance_table)

    # Measure execution times for a range of node counts
    node_counts = range(5, 100, 5)
    dv_times = []
    dijkstra_times = []

    for count in node_counts:
        # Generate a graph with 'count' nodes
        random_nodes, random_edges = generate_random_graph(count, [])
        dv_times.append(measure_dv_algorithm(random_nodes, random_edges))
        dijkstra_times.append(measure_dijkstra_algorithm(random_nodes, random_edges))

    # Plot the execution times
    plot_execution_times(dv_times, dijkstra_times, node_counts)


if __name__ == '__main__':
    main()
