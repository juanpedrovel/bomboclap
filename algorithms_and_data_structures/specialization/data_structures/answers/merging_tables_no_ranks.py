# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
parent = list(range(0, n))
ans = int(max(lines))


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
    
    else:
        global ans
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        if ans < lines[realDestination]:
             ans = lines[realDestination]

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
