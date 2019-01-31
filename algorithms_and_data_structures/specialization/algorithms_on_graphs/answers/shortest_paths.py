#Uses python3

import sys
from queue import Queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    lens = len(adj)
    price = [[float('inf'), x] for x in range(lens)]
    price[s][0] = 0
    distance[s] = 0
    q = Queue()
    q.put(s)
    is_reachable(q, reachable, adj)
    for k in range(lens):
        for i in range(lens):
            childs = adj[i]
            for j in range(len(childs)):
                if price[childs[j]][0] > price[i][0] + cost[i][j]:
                    price[childs[j]][0] = price[i][0] + cost[i][j]
                    if k == lens - 1:
                        q.put(childs[j])
                elif k == lens - 1:
                    distance[childs[j]] = price[childs[j]][0]
    breath_first(q, shortest, adj)

def breath_first(q, shortest, adj):
    while not q.empty():
        u = q.get()
        shortest[u] = 0
        for i in adj[u]:
            if shortest[i] == 1:
                q.put(i)

def is_reachable(q, reachable, adj):
    while not q.empty():
        u = q.get()
        reachable[u] = 1
        for i in adj[u]:
            if reachable[i] == 0:
                q.put(i)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

