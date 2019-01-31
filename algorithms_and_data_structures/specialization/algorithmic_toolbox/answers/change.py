# Uses python3
import sys

def get_change(m):
    
    d, n, c = 10, 5, 1
    coins = 0

    while m >= d:
        coins += 1
        m = m - d

    while m >= n:
        coins += 1
        m = m - n

    while m >= c:
        coins += 1
        m = m - c

    return(coins)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))