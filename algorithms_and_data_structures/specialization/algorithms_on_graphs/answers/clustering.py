#Uses python3
import sys
import math

class Disjoint_set:
    def __init__(self, size):
        self.size = size
        self.parents = [x for x in range(self.size)]
        self.rank = [0] * self.size

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


def clustering(x, y, k):
    lens = len(x)
    result = 0.0
    distances = sort_edges(x, y)
    D = Disjoint_set(lens)
    counter = 0
    points = []
    for i in distances:
        if counter == lens - 1:
            break
        one = i[1][0]
        two = i[1][1]
        if D.find(one) != D.find(two):
            if counter >= lens - k:
                points.append(i)
            D.union(one, two)
            counter += 1
    d = min(points)
    return d[0]

def sort_edges(x, y):
    distances = []
    lens = len(x)
    for i in range(lens):
        for j in range(i + 1, lens):
            distances.append((math.sqrt((x[i] - x[j])**2 + (y[i]- y[j])**2), [i,j]))
    distances.sort()
    return distances


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
