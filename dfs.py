from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Remove this line if the graph is directed

    def DFSutil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSutil(neighbor, visited)

    def dfs(self, v):
        visited = set()
        self.DFSutil(v, visited)

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

start_vertex = int(input("Enter starting vertex for DFS: "))
print(f"Following DFS from '{start_vertex}': ")
g.dfs(start_vertex)
