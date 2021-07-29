from collections import defaultdict


# The structure to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Find the parent of the vertices
    def find_parent(self, i, parent):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent[i], parent)

    # Sets the parent of each vertex
    def union(self, parent, x, y):
        parent[x] = y

    # Check if there is a cycle
    # Return True if there is one and False if isn't
    def check_cycle(self):
        parent = [-1] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(i, parent)
                y = self.find_parent(j, parent)

                if x == y:
                    return True

                self.union(parent, x, y)


def main():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)

    if g.check_cycle():
        print('Cycle')
    else:
        print('No cycles')


if __name__ == '__main__':
    main()
