# Uses python3
mins = []
maxs = []
numbers = []
operations = []

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    
    for i in range(len(dataset)):
        if i % 2 == 0:
            numbers.append(int(dataset[i]))
        else:
            operations.append(dataset[i])

    lenn = len(numbers)
    leno = len(operations)

    for i in range(lenn):
        mins.append([])
        maxs.append([])
        for j in range(lenn):
            mins[i].append([])
            maxs[i].append([])

    for i in range(lenn):
        mins[i][i] = numbers[i]
        maxs[i][i] = numbers[i]
    for s in range(1, lenn):
        for i in range(lenn - s):
            j = i + s
            mins[i][j], maxs[i][j] = MinAndMax(i,j)

    return maxs[0][lenn - 1]

def MinAndMax(i,j):
    m = float('inf')
    M = float('-inf')

    for k in range(i, j):
        a = evalt(maxs[i][k], maxs[k + 1][j], operations[k])
        b = evalt(maxs[i][k], mins[k + 1][j], operations[k])
        c = evalt(mins[i][k], maxs[k + 1][j], operations[k])
        d = evalt(mins[i][k], mins[k + 1][j], operations[k])
        m = min(m, a, b, c, d)
        M = max(M, a, b, c, d)
    return(m, M)

if __name__ == "__main__":
    print(get_maximum_value(input()))
