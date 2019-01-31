# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    all = []
    for i in starts:
        all.append((i, 'l'))
    for i in ends:
        all.append((i, 'r'))
    for i in range(len(points)):
        all.append((points[i], 'p', i))

    all = merge_sort(all)

    segments_open = 0
    for x in all:
        if x[1] == 'l':
            segments_open += 1
        elif x[1] == 'r':
            segments_open -= 1
        else:
            cnt[x[2]] = segments_open

    return cnt

def merge_sort(a):
    if len(a) == 1:
        return a
    m = len(a) // 2
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])
    b = []
    for i in range(len(a)):
        if left and right:
            if left[0][0] < right[0][0]:
                b.append(left.pop(0))
            elif left[0][0] == right[0][0]:
                if left[0][1] == 'l' or (left[0][1] == 'p' and right[0][1] == 'r'):
                    b.append(left.pop(0))
                else:
                    b.append(right.pop(0))
            else:
                b.append(right.pop(0))
        else:
            b += left + right
            break
    return(b)
            

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
