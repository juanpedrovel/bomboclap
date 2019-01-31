#Uses python3

import sys
from queue import Queue

def distance(adj, s, t):
    distance = [float('inf')] * len(adj)
    distance[s] = 0
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for i in adj[u]:
            if distance[i] == float('inf'):
                q.put(i)
                distance[i] = distance[u] + 1
    if distance[t] == float('inf'):
        return -1
    else:
        return distance[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
