#Uses python3

import sys

class Graph:
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.visited = [False] * self.size
        self.sinks = [False] * self.size
 
    def check_cc(self):
        for i in range(self.size):
            if self.visited[i] == False:
                a = self.acyclic(i)
                if a == True:
                    return 1
        return 0

    def acyclic(self, x):
        self.visited[x] = True
        nb = self.adj[x]
        for i in nb:
            if self.visited[i] == False:
                if self.acyclic(i) == 1:
                    return 1
            else:
                if self.sinks[i] == False:
                    return 1
        self.sinks[x] = True
        return 0



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
    print(G.check_cc())
