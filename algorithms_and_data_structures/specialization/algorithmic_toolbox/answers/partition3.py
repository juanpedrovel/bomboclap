# Uses python3
import sys

matrix = []

def partition(A):
    portion = sum(A)
    if not portion % 3 == 0:
        return 0
    portion = portion // 3
    A.insert(0,0)
    B = partition_def(A, portion)
    if B == 0:
        return 0
    else:
        C = partition_def(B, portion)
        if C == 0:
            return 0
        else:
            return 1

def partition_def(A, portion):
    lena = len(A)
    for i in range(lena):
        matrix.append([])
        for j in range(portion + 1):
            matrix[i].append([])
    for i in range(lena):
        for j in range(portion + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = check(i,j)
                if matrix[i][j] == portion:
                    items = []
                    optimal_solution(i, j, A, items)
                    B = list(A)
                    for x in items:
                        B.pop(x)
                        return (B)            
    return 0


def optimal_solution(i, j, A, items):
    if matrix[i][j] == 0:
        return
    elif not matrix[i][j] == matrix[i - 1][j]:
        items.append(i)
        optimal_solution(i - 1, j - A[i], A, items)
    else:
        optimal_solution(i - 1, j, A, items)


def check(i, j):
    if A[i] <= j and (A[i] + matrix[i-1][j-A[i]]) > matrix[i-1][j]:
        value = A[i] + matrix[i-1][j-A[i]]
    else:
        value = matrix[i-1][j]
    return value


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition(A))

