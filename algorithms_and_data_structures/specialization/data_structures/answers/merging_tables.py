# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))


def getParent(table):
    nums = []
    while parent[table] != table:
        nums.append(table)
        table = parent[table]
    for i in nums:
        parent[i] = table
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False
    
    if rank[realDestination] >= rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1
    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    ans = max(lines)
    print(ans)
    
