from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Remove this line if the graph is directed

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def printGraph(self):
        for vertex in self.graph:
            neighbors = ' '.join(map(str, self.graph[vertex]))
            print(f"{vertex} -> {neighbors}")

g = Graph()
no = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(no):
    u, v = map(int, input().split())
    g.addEdge(u, v)

print("Graph Representation:")
g.printGraph()

start_vertex = int(input("Enter starting vertex for BFS: "))
print(f"Following BFS from '{start_vertex}': ")
g.bfs(start_vertex)
