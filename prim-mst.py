from collections import defaultdict
from sys import maxsize
from timeit import default_timer as timer

start = timer()


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = defaultdict(list)
        self.prim_subsets = []

    def add_edge(self, u, v, w):
        self.edges[u - 1].append([v - 1, w])
        self.edges[v - 1].append([u - 1, w])

    def min_key(self):
        min_weight = maxsize
        min_index = None

        for i in range(self.V):
            if self.prim_subsets[i].key < min_weight and self.prim_subsets[i].used is False:
                min_weight = self.prim_subsets[i].key
                min_index = i
        return min_index

    def prim_mst(self):
        resulting_mst = []
        [self.prim_subsets.append(Subset(False, None, maxsize)) for _ in range(self.V)]
        self.prim_subsets[0].parent = -1
        self.prim_subsets[0].key = 0

        for _ in range(self.V):
            u = self.min_key()

            self.prim_subsets[u].used = True
            if self.prim_subsets[u].parent != -1:
                resulting_mst.append([self.prim_subsets[u].parent, u, self.prim_subsets[u].key])

            for j in self.edges[u]:
                subset = self.prim_subsets[j[0]]
                edge_weight = j[1]
                if 0 < edge_weight < subset.key and subset.used is False:
                    subset.key = edge_weight
                    subset.parent = u

        minimum_cost = 0
        for u, v, weight in resulting_mst:
            minimum_cost += weight
            print(f"{u + 1} -- {v + 1} == {weight}")
        print(f"Minimum Spanning Tree = {minimum_cost}")


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

    elapsed_time = timer() - start
    print(elapsed_time)


if __name__ == '__main__':
    main()
