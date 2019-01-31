#Uses python3

import sys

matrix = []

def lcs2(x, y):
    a = list(x)
    b = list(y)
    a.insert(0, 0)
    b.insert(0, 0)
    
    lena = len(a)
    lenb = len(b)

    for i in range(lena):
        matrix.append([])
        for j in range(lenb):
            matrix[i].append([])
    
    for i in range(lena):
        for j in range(lenb):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif a[i] == b[j]:
                matrix[i][j] = check_sq(i, j, 1)
            else:
                matrix[i][j] = check_sq(i, j, 0)
    return matrix[lena - 1][lenb - 1]

def check_sq(i, j, n):
    
    if n == 1:
        slot = matrix[i-1][j-1] + 1
    else:
        slot = max(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
    return slot


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
