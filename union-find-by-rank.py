from collections import defaultdict


# The structure to represent the graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)


# The structure to represent a subset
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


# This function unite sets
# The bigger rank becomes the parent of the smaller one
# If both ranks are the same then make one as parent of the other
# and increment its rank by one
def union(subsets, u, v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


# Find the set's parent and make the path compression if needed
def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


# Check if there is an cycle in the graph
def is_cycle(graph):
    subsets = []

    for u in range(graph.V):
        subsets.append(Subset(u, 0))

    # Iterate over all edges of the graph
    # If the parents of both vertices are the same
    # Then there is a cycle
    for i in graph.edges:
        x = find(subsets, i)

        for j in graph.edges[i]:
            y = find(subsets, j)

            if x == y:
                return True

            union(subsets, x, y)


def main():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)

    if is_cycle(g):
        print('Cycle')
    else:
        print('Not Cycle')


if __name__ == '__main__':
    main()
