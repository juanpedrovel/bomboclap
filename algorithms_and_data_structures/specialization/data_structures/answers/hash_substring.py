# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S,prime,x):
    hash = 0
    for i in reversed(S):
        hash = (hash*x + ord(i)) % prime
    return hash
    
def RabinKarp(P, T):
    results = []
    lent = len(T)
    lenp = len(P)
    prime = 1000000007
    x = 263
    phash = PolyHash(P, prime, x)
    H = Precompute(T, P, x, prime)
    for i, h in enumerate(H):
        if h == phash:
            if get_occurrences(T[i:i+lenp], P):
                results.append(i)

    return results


def Precompute(T, P, x, prime):
    lent = len(T)
    lenp = len(P)
    s = T[lent - lenp : ]
    H = [None] * (lent - lenp + 1)
    H[lent - lenp] = PolyHash(s, prime, x)
    
    y = 1
    for i in range(lenp):
        y = (x * y) % prime

    for i in range(lent - lenp - 1, -1, -1):
        H[i] = (x*H[i + 1] + ord(T[i]) - y*ord(T[i + lenp])) % prime

    return H

def get_occurrences(text, patern):
    if patern == text:
        return True
    else:
        return False


if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

