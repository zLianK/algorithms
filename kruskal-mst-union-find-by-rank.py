from timeit import default_timer as timer

start = timer()


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

        self.subsets = []
        for u in range(self.V):
            self.subsets.append(Subset(u, 0))

    def add_edge(self, u, v, w):
        self.edges.append([u - 1, v - 1, w])

    def is_cycle(self, edge_index):
        x = self.find(self.edges[edge_index][0])
        y = self.find(self.edges[edge_index][1])

        if x == y:
            return True

        self.union(x, y)

    def union(self, u, v):
        if self.subsets[u].rank > self.subsets[v].rank:
            self.subsets[v].parent = u
        elif self.subsets[v].rank > self.subsets[u].rank:
            self.subsets[u].parent = v
        else:
            self.subsets[v].parent = u
            self.subsets[u].rank += 1

    def find(self, node):
        if self.subsets[node].parent != node:
            self.subsets[node].parent = self.find(self.subsets[node].parent)
        return self.subsets[node].parent

    def kruskal_mst(self):
        edge_index = 0
        edge_counter = 0
        mst = []
        self.edges = sorted(self.edges, key=lambda item: item[2])

        while edge_counter < self.V - 1:
            if not self.is_cycle(edge_index):
                edge_counter += 1
                mst.append(self.edges[edge_index])
            edge_index += 1

        minimum_cost = 0
        for u, v, weight in mst:
            minimum_cost += weight
            print(f"{u + 1} -- {v + 1} == {weight}")
        print(f"Minimum Spanning Tree = {minimum_cost}")


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


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

    g.kruskal_mst()

    elapsed_time = timer() - start
    print(elapsed_time)


if __name__ == '__main__':
    main()
