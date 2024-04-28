import sys

def bellman_ford(graph, source):
    n = len(graph)
    dist = [sys.maxsize] * n
    pred = [None] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, weight in enumerate(graph[u]):
                if weight != float('inf'):
                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        pred[v] = u

    return dist, pred

def print_shortest_path(source, dest, pred, vertex_names, dist):
    if pred[dest] is None:
        print(f"No path from {vertex_names[source]} to {vertex_names[dest]}")
        return

    path = [dest]
    curr = dest
    while curr != source:
        curr = pred[curr]
        path.append(curr)

    path.reverse()
    vertices = [vertex_names[v] for v in path]
    values = [dist[v] for v in path]

    print(f"Shortest path from {vertex_names[source]} to {vertex_names[dest]}: {' -> '.join(vertices)}")
    print("Values along the path:", values)

# Example from textbook
graph = [
    [0, 7, float('inf'),6, float('inf')],
    [float('inf'), 0 , -3, float('inf'), 9],
    [float('inf'), float('inf'),0, -2,float('inf')],
    [float('inf'), 6, 5,0, -4],
    [2, float('inf'), 7, float('inf'),0]
]

vertex_names = {0: 's', 1: 'y', 2: 'x', 3: 't', 4: 'z'} 
source = 0  # Vertex s
dest = 4  # Vertex z

dist, pred = bellman_ford(graph, source)

print_shortest_path(source, dest, pred, vertex_names, dist)
