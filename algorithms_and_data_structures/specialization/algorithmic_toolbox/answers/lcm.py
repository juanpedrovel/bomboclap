# Uses python3

import sys

def lcm(a, b):
    x = (a * b) // gcd(a, b)
    return int(x)

def gcd(a, b):
    if b == 0:
        return a
    
    else:
        alpha = a % b
        return gcd(b, alpha)    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a,b))
