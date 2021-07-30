from collections import defaultdict
from sys import maxsize


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = defaultdict(list)
        self.prim_subsets = []

    def add_edge(self, u, v, w):
        self.edges[u].append([v, w])

    def min_key(self):
        pass

    def prim_mst(self):
        [self.prim_subsets.append(Subset(maxsize, None, False)) for _ in range(self.V)]
        self.prim_subsets[0].parent = -1
        


class Subset:
    def __init__(self, used, parent, key):
        self.used = used
        self.parent = parent
        self.key = key


def main():
    g = Graph(16)
    g.add_edge(1, 16, 4)
    g.add_edge(1, 10, 8)
    g.add_edge(2, 9, 8)
    g.add_edge(2, 11, 1)
    g.add_edge(3, 10, 11)
    g.add_edge(3, 12, 7)
    g.add_edge(4, 11, 2)
    g.add_edge(4, 13, 6)
    g.add_edge(5, 12, 7)
    g.add_edge(5, 14, 2)
    g.add_edge(6, 13, 4)
    g.add_edge(6, 15, 14)
    g.add_edge(7, 14, 9)
    g.add_edge(7, 16, 10)
    g.add_edge(8, 15, 4)
    g.add_edge(8, 9, 8)
    g.add_edge(9, 14, 8)
    g.add_edge(9, 12, 1)
    g.add_edge(10, 15, 11)
    g.add_edge(10, 13, 7)
    g.add_edge(11, 14, 2)
    g.add_edge(11, 16, 6)
    g.add_edge(12, 15, 7)
    g.add_edge(13, 16, 2)

    g.prim_mst()


if __name__ == '__main__':
    main()
