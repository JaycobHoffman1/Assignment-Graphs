import heapq

# Task 1: Define Graph Representation

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

    # Task 2: Implement Dijkstra's Algorithm

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Task 3: Test the Algorithm Implementation

graph1 = Graph()
graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')
graph1.add_edge('A', 'B', 5)
graph1.add_edge('B', 'C', 3)
graph1.add_edge('A', 'C', 10)
graph2 = Graph()
graph2.add_vertex('A')
graph2.add_vertex('B')
graph2.add_vertex('C')
graph2.add_edge('A', 'B', 10)
graph2.add_edge('B', 'C', 5)
graph2.add_edge('A', 'C', 3)
distances1 = graph1.dijkstra('A')
distances2 = graph2.dijkstra('A')

print("Shortest distances from vertex A for Graph 1:", distances1)
print("Shortest distances from vertex A for Graph 2:", distances2)

# Task 4: Analyze Time and Space Complexity

"""
According to___, when used with priority queue like those used here, Dijkstra's algorithm has a time complexity of O((V + E) log V)
and a space complexity of O(V), with V represeting the graph's vertices and E representing its edges. In order to lower the algorithm's
time complexity to O(V^2), we could use it with an array 
as opposed to a priority queue ("Time and Space Complexity of Dijkstra's Algorithm", 2024).

Work Cited
"Time and Space Complexity of Dijkstra's Algorithm." Geeks4Geeks. 2024, February 9. 
https://www.geeksforgeeks.org/time-and-space-complexity-of-dijkstras-algorithm/
"""