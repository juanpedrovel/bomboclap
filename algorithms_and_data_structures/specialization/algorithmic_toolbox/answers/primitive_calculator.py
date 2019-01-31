# Uses python3
import sys

def optimal_sequence(n):
    sequence = [(0, 'sum')] 
    for i in range(1, n + 1):
        opt1 = (sequence[i - 1][0] + 1, 'sum')
        opt2 = (float('inf'), 'none')
        opt3 = (float('inf'), 'none')
        if i % 2 == 0:
            opt2 = (sequence[i // 2][0] + 1, 'two')
        if i % 3 == 0:
            opt3 = (sequence[i // 3][0] + 1, 'three')
        sequence.append(min(opt1, opt2, opt3))
    x = [n]
    a = [n, sequence[n][1]]
    while a[0] > 1:
        if a[1] == 'sum':
            a[0], a[1] = a[0] - 1, sequence[a[0] - 1][1]
        elif a[1] == 'two':
            a[0], a[1] = a[0] // 2, sequence[a[0] // 2][1]
        elif a[1] == 'three':
            a[0], a[1] = a[0] // 3, sequence[a[0] // 3][1]
        x.append(a[0])

    return reversed(x)

    

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
