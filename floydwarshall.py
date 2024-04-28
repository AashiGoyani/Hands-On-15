def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Make a copy of the graph to store shortest distances

    # Print the initial matrix (D(0))
    print("D(0):")
    for row in graph:
        print([x if x != float('inf') else 'inf' for x in row])
    print()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Print the D(k) matrix after each iteration
        print(f"D({k+1}):")
        for row in dist:
            print([x if x != float('inf') else 'inf' for x in row])
        print()

# Given graph represented as an adjacency matrix
graph = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

# Perform Floyd-Warshall algorithm
floyd_warshall(graph)
