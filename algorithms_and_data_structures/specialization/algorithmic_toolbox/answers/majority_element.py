# Uses python3
import sys

def get_majority_element(a):

    if len(a) == 1:
        return (True, a[0])

    else:
        left = get_majority_element(a[:len(a)//2])
        right = get_majority_element(a[len(a)//2:])
        if left == right:
            return left
        if left[0] or right[0]:
            countr = 0
            countl = 0
            for i in a:
                if i == left[1]:
                    countl += 1
                if i == right[1]:
                    countr += 1

            if countl > len(a) // 2:
                return left
            elif countr > len(a) // 2:
                return right
        
    return (False, -1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != (False, -1):
        print(1)
    else:
        print(0)
