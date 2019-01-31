# Uses python3
import sys

def binary_search(a, x, left, right):
    m = (right + left) // 2
    if a[left] == x:
        return left
    elif a[right-1] == x:
        return right - 1
    elif a[m] == x:
        return m
    else:
        while left < right:
            if x > a[m]:
                return binary_search(a, x, m+1, right-1)
            else:
                return binary_search(a, x, left + 1, m)
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)), end = ' ')
