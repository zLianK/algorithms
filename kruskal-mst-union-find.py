from timeit import default_timer as timer

start = timer()


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u - 1, v - 1, w])

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def is_cycle(self, parent, index):

        x = self.find_parent(parent, self.graph[index][0])
        y = self.find_parent(parent, self.graph[index][1])

        if x == y:
            return True
        else:
            self.union(parent, x, y)

        return False

    def kruskal_mst(self):

        parent = [-1] * self.V
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        i = 0
        e = 0

        while e < self.V - 1:
            if not self.is_cycle(parent, i):
                e += 1
                result.append(self.graph[i])
            i += 1

        minimum_cost = 0
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u + 1} -- {v + 1} == {weight}")
        print(f"Minimum Spanning Tree = {minimum_cost}")


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
