# Uses python3
import sys

matrix = []

def optimal_weight(W, w):
    w.insert(0, 0)
    lenw = len(w)
    for i in range(lenw):
        matrix.append([])
        for j in range(W + 1):
            matrix[i].append([])

    for i in range(lenw):
        for j in range(W + 1):
            if j == 0 or i == 0:
                matrix[i][j] = 0
            elif w[i] <= j:
                matrix[i][j] = max(w[i] + matrix[i - 1][j-w[i]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[lenw - 1][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
