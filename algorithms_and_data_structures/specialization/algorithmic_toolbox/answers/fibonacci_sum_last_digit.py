# Uses python3
import sys

f = [0, 1]
p = [0, 1]

def fibonacci_sum_last_digit(n):
    pisano10 = pisano(10)
    if n >= pisano10:
        x = n // pisano10
        y = x * sum(p[:pisano10 + 1]) + sum(p[:(n % pisano10) + 1])
        return y % 10
    else:
        return sum(p[:n + 1])
    
def fibonacci(n):
    if n >= len(f):
        for i in range(len(f), n + 1):
            f.append(f[i - 1] + f[i - 2])
    return(f[n])
    
def pisano(m):
    if m >= len(p):
        i = len(p)
        while True:
            p.append(fibonacci(i) % m)
            if p[i] == 1 and p[i-1] == 0 and p[i-2] == 1:
                break
            i+=1
    return i-1    
    
if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum_last_digit(n))