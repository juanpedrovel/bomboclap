#Uses python3
import sys
import queue
from copy import deepcopy

class Graph:
    def __init__(self, adj, inv, cost):
        self.adj = adj
        self.size = len(adj)
        self.inverse = inv
        self.visited = [False] * self.size
        self.visited_inv = [False] * self.size
        self.topolist_inv = []
        self.scc = []
        self.cost = cost
        
    def check_scc(self):
        self.check_cc_inv()
        for i in range(self.size - 1, -1, -1):
            s = self.topolist_inv[i]
            if self.visited[s] == False:
                self.explore(s)
                self.scc.append(s)
 
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

    def negative_cycle(self):
        price = [[float('inf'), x] for x in range(self.size)]
        for i in self.scc:
            price[i][0] = 0
        for k in range(self.size):
            counter = 0
            for i in range(self.size):
                childs = self.adj[i]
                for j in range(len(childs)):
                    if price[childs[j]][0] > price[i][0] + self.cost[i][j]:
                        price[childs[j]][0] = price[i][0] + self.cost[i][j]
                        counter += 1
            if counter == 0:
                return 0
        return 1
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    inv = deepcopy(adj)
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        inv[b - 1].append(a - 1)
        cost[a - 1].append(w)
    G = Graph(adj, inv, cost)
    G.check_scc()
    print(G.negative_cycle())
