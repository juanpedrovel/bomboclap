#Uses python3

import sys

class Graph:
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.visited = [False] * self.size
        self.sinks = [False] * self.size
        self.topolist = []
 
    def check_cc(self):
        for i in range(self.size):
            if self.visited[i] == False:
                self.explore(i)
        return

    def explore(self, x):
        self.visited[x] = True
        nb = self.adj[x]
        for i in nb:
            if self.visited[i] == False:
                self.explore(i)
        self.topolist.append(x)
        return

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    G = Graph(adj)
    G.check_cc()
    ts = G.topolist
    for x in range(n - 1, -1, -1):
        print(ts[x] + 1, end=' ')

