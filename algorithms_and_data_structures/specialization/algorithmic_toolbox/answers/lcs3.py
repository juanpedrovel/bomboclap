#Uses python3

import sys

matrix = []

def lcs3(a, b, c):
    a.insert(0, 0)
    b.insert(0, 0)
    c.insert(0, 0)
      
    lena = len(a)
    lenb = len(b)
    lenc = len(c)

    for i in range(lena):
        matrix.append([])
        for j in range(lenb):
            matrix[i].append([])
            for z in range(lenc):
                matrix[i][j].append([])
    
    for z in range(lenc):
        for i in range(lena):
            for j in range(lenb):
                if z == 0 or i == 0 or j == 0:
                    matrix[i][j][z] = 0
                elif a[i] == b[j] == c[z]:
                    matrix[i][j][z] = check_sq(i, j, z, 1)
                else:
                    matrix[i][j][z] = check_sq(i, j, z, 0)
    return matrix[-1][-1][-1]

def check_sq(i, j, z, n):
    if n == 1:
        slot = matrix[i-1][j-1][z-1] + 1
    else:
        slot = max(matrix[i-1][j][z], matrix[i][j-1][z], matrix[i][j][z-1])
    return slot


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
