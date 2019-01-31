# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l + 1
    g = r
    k = j
    while j <= g:
        if a[j] < x:
            a[j], a[k] = a[k], a[j]
            k+=1
            j+=1
        elif a[j] == x:
            j += 1
        elif a[j] >  x:
            while a[g] > x and j < g:
                g -= 1
            a[j], a[g] = a[g], a[j]
            g -= 1
                    
    k -= 1
    a[l], a[k] = a[k], a[l]
    return (k, j)


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, s = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, s, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
