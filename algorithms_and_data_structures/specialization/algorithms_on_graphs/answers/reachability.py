#Uses python3

import sys

class Graph:
    def __init__(self, adj):
        self.adj = adj
        self.visited = [False] * len(adj)


    def reach(self, x, y):
        self.explore(x)
        if self.visited[y] == True:
            return 1
        else:
            return 0

    def explore(self, x):
        self.visited[x] = True
        nb = self.adj[x]
        for i in nb:
            if self.visited[i] == False:
                self.explore(i)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    G = Graph(adj)
    print(G.reach(x, y))
