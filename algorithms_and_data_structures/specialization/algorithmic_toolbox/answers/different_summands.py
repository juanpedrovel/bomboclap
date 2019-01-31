# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    x = 0
    for i in range(1, n + 1):
        if x + i > n:
            summands[-1] += n - x
            break
        else:
            x += i
            summands.append(i)
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
