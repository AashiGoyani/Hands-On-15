import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example from textbook
graph_a = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'z': 4},
    'x': {'z': 6},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'z': {'s': 7, 'x': float('inf')}
}

print("Example (a):")
result = dijkstra(graph_a, 's')
print(result)