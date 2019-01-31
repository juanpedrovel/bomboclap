#Uses python3

import sys
from copy import deepcopy

sys.setrecursionlimit(200000)

class Graph:
    def __init__(self, adj, inv):
        self.adj = adj
        self.size = len(adj)
        self.inverse = inv
        self.visited = [False] * self.size
        self.visited_inv = [False] * self.size
        self.topolist_inv = []
        self.scc = 0
        
    def check_scc(self):
        self.check_cc_inv()
        for i in range(self.size - 1, -1, -1):
            s = self.topolist_inv[i]
            if self.visited[s] == False:
                self.explore(s)
                self.scc += 1
        return self.scc
 
    def check_cc_inv(self):
        for i in range(self.size):
            if self.visited_inv[i] == False:
                self.explore_inv(i)
        return

    def explore_inv(self, x):
        self.visited_inv[x] = True
        nb = self.inverse[x]
        for i in nb:
            if self.visited_inv[i] == False:
                self.explore_inv(i)
        self.topolist_inv.append(x)
        return

    def explore(self, x):
        self.visited[x] = True
        nb = self.adj[x]
        for i in nb:
            if self.visited[i] == False:
                self.explore(i)
        return


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    inv = deepcopy(adj)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        inv[b - 1].append(a - 1)
    G = Graph(adj, inv)
    print(G.check_scc())
