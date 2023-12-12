import heapq
from collections import deque


class Graph:
    def __init__(self):
        self.graph = []

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.append(vertex)

    def add_edge(self, from_vertex, to_vertex, weight=None):
        self.graph.append((from_vertex, to_vertex, weight))

    def display_graph(self):
        for edge in self.graph:
            print(f"{edge[0]} {edge[1]} {edge[2]}")

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
                neighbors = [edge[1] for edge in self.graph if edge[0] == current_vertex]
                queue.extend(neighbors)

    def prim(self, start_vertex):
        visited = set()
        mst = []
        priority_queue = [(0, start_vertex, None)]

        while priority_queue:
            weight, current_vertex, parent = heapq.heappop(priority_queue)
            if current_vertex not in visited:
                visited.add(current_vertex)
                if parent is not None:
                    mst.append((parent, current_vertex, weight))
                neighbors = [(edge[2], edge[1]) for edge in self.graph if edge[0] == current_vertex]
                for neighbor_weight, neighbor_vertex in neighbors:
                    if neighbor_vertex not in visited:
                        heapq.heappush(priority_queue, (neighbor_weight, neighbor_vertex, current_vertex))

        return mst


if __name__ == "__main__":
    my_graph = Graph()

    my_graph.add_edge(1, 2, 3)
    my_graph.add_edge(1, 3, 1)
    my_graph.add_edge(2, 3, 1)
    my_graph.add_edge(2, 4, 4)
    my_graph.add_edge(3, 4, 5)

    print("Graph:")
    my_graph.display_graph()

    print("\nBFS traversal starting from vertex 1:")
    my_graph.bfs(1)

    mst_edges = my_graph.prim(1)

    print("\n\nMinimum Spanning Tree (Prim's Algorithm):")
    for edge in mst_edges:
        print(f"{edge[0]} {edge[1]} {edge[2]}")