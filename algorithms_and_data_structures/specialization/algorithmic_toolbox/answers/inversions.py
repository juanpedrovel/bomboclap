# Uses python3
import sys

def get_number_of_inversions(a):
    number_of_inversions = 0
    if len(a) == 1:
        return (number_of_inversions, a)
    ave = len(a) // 2
    l1, left = get_number_of_inversions(a[:ave])
    r1, right = get_number_of_inversions(a[ave:])

    number_of_inversions += l1 + r1

    b = []
    l = 0
    r = 0
    for i in range(len(a)):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                b.append(left[l])
                l += 1
            else:
                b.append(right[r])
                number_of_inversions += len(left) - l
                r += 1
        elif l == len(left):
            b += right[r:]
            break
        else:
            b += left[l:]
            break
    return (number_of_inversions, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[0])
