# Uses python3
from enum import Enum

matrix = []


class Operation(Enum):

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())

def deletion(i, j):
    return ((matrix[i - 1][j][0] + 1), Operation.DELETED)


def insertion(i, j):
    return ((matrix[i][j - 1][0] + 1), Operation.INSERTED)


def subs(i, j, a, b):
    if a[i - 1] == b[j - 1]:
        return ((matrix[i - 1][j - 1][0]), Operation.SUBSTITUTED)
    else:
        return ((matrix[i - 1][j - 1][0] + 1), Operation.SUBSTITUTED)


def edit_distance(a, b):

    for i in range(len(a) + 1):
        matrix.append([])
        for j in range(len(b) + 1):
            matrix[i].append([])
            if i == 0 and j == 0:
                matrix[i][j] = (0, None)
            elif i == 0:
                matrix[i][j] = (j, Operation.INSERTED)
            elif j == 0:
                matrix[i][j] = (i, Operation.DELETED)

 
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            matrix[i][j] = min(deletion(i, j),
                               insertion(i, j), subs(i, j, a, b),
                               key=lambda x: x[0])

    return matrix[-1][-1][0]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
