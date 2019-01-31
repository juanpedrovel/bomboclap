#Uses python3

import sys

def largest_number(a):
    res = ""
    b = a

    while len(b) > 0:
        max = 0
        for x in b:
            max = best_num(x, max)
        res += str(max)
        b.remove(str(max))
            
    return int(res)

def best_num(x, y):
    
    if x == y:
        return x

    x = str(x)
    y = str(y)

    lx = len(x)
    ly = len(y)

    if lx == ly:
        return max(x, y)

    for i in range(min(lx, ly)):
        if x[i] > y[i]:
            return x
        elif y[i] > x[i]:
            return y

    if lx > ly:
        if best_num((x[ly:]), y) == y:
            return y
        else:
            return x
    else:
        if best_num(x, y[lx:]) == x:
            return x
        else:
            return y

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
