from collections import deque


class Graph:
    def __init__(self):
        self._adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self._adjacency:
            self._adjacency[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self._adjacency[vertex1].append(vertex2)
        self._adjacency[vertex2].append(vertex1)

    def neighbors(self, vertex) -> list:
        return self._adjacency.get(vertex, [])

    def bfs(self, start) -> list:
        visited = []
        queue = deque()

        visited.append(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

        return visited

    def dfs(self, start) -> list:
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            vertex = stack.pop()
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)

        return visited

    def __str__(self):
        result = ""
        for vertex, neighbors in self._adjacency.items():
            result += f"{vertex} → {neighbors}\n"
        return result


def run_test():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")

    print(g)
    print(g.bfs("A"))
    print(g.dfs("A"))
