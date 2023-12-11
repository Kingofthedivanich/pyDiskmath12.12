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

    def kruskal(self):
        sorted_edges = sorted(self.graph, key=lambda edge: edge[2] if edge[2] is not None else float('inf'))

        parent = {vertex: vertex for vertex in set.union(*map(set, [(edge[0], edge[1]) for edge in sorted_edges]))}

        def find_parent(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find_parent(parent[vertex])
            return parent[vertex]

        def union(v1, v2):
            root1 = find_parent(v1)
            root2 = find_parent(v2)
            parent[root1] = root2

        mst = []

        for edge in sorted_edges:
            v1, v2, weight = edge
            if find_parent(v1) != find_parent(v2):
                mst.append(edge)
                union(v1, v2)

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

    mst_edges = my_graph.kruskal()

    print("\n\nMinimum Spanning Tree (Kruskal's Algorithm):")
    for edge in mst_edges:
        print(f"{edge[0]} {edge[1]} {edge[2]}")
