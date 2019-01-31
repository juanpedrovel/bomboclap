# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    minc = [float('inf')] * (m + 1)
    min_coins = min_num_coins(m, coins, minc)
    return min_coins

def min_num_coins(m, coins, minc):
    minc[0] = 0
    for i in range(1, m + 1):
        for j in coins:
            if j <= i:
                coins_temp = minc[i - j] + 1
                if coins_temp < minc[i]:
                    minc[i] = coins_temp
    return minc[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
