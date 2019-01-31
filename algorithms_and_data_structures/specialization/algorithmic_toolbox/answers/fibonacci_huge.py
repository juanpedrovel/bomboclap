# Uses python3
import sys

f = [0, 1]
p = [0, 1]

def fibonacci_huge(n, m):
    if m > n:
        return fibonacci(n) % m
    
    else:
        x = n % pisano(m)
        return fibonacci(x) % m
        

def pisano(m):
    if m >= len(p):
        i = len(p)
        while True:
            p.append((p[i - 1] + p[i - 2]) % m)
            if p[i] == 1 and p[i-1] == 0 and p[i-2] == 1:
                break
            i+=1
    return i-1


def fibonacci(n):
    if n >= len(f):
        for i in range(len(f), n + 1):
            f.append(f[i - 1] + f[i - 2])
    return(f[n])
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))