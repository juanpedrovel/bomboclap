#Uses python3
import sys
import math
import random

def minimum_distance(x, y):
    points = [0] * len(x)
    pointsy = [0] * len(x)
    for i in range(len(x)):
        points[i] = (x[i], y[i])
        pointsy[i] = (x[i], y[i])
    randomized_quick_sort(points, 0, len(points)-1, 0)
    randomized_quick_sort(pointsy, 0, len(pointsy)-1, 1)
    s = check_distance(points, pointsy)
    return s

def partition2(a, l, r, xy):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i][xy] <= x[xy]:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r, xy):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r, xy)
    randomized_quick_sort(a, l, m - 1, xy);
    randomized_quick_sort(a, m, r, xy);

def check_distance(a, ay):
    len_ay = len(ay)
    if len_ay <= 3:
        return brute(a)
    m = len_ay // 2
    left = a[:m]
    right = a[m:]
    left_y = []
    right_y = []

    for i in range(len_ay):
        if ay[i] in left:
            left_y.append(ay[i])
        else:
            right_y.append(ay[i])

    min_l = check_distance(left, left_y)
    min_r = check_distance(right, right_y)
    min_distance = min(min_l, min_r)
    
    middle_axis = a[m][0]
    all_copy = []

    for i in range(len_ay):
        dist_to_axis = abs(ay[i][0] - middle_axis)
        if dist_to_axis < min_distance:
            all_copy.append(ay[i])

    all_copy_len = len(all_copy)
    for i in range((all_copy_len) - 1):
        for j in range(1, 6):
            if i + j >= (all_copy_len):
                break
            elif (all_copy[i] in left and all_copy[i+j] in right) or (all_copy[i] in right and all_copy[i+j] in left):
                distance = dist(all_copy[i], all_copy[i + j])
                if distance < min_distance:
                    min_distance = distance
                    if min_distance == 0:
                        return min_distance   
    return min_distance

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute(a):
    len_a = len(a)
    min_distance = float('inf')
    for i in range(len_a - 1):
        for j in range(1, len_a):
            if i + j >= len_a:
                break
            d = dist(a[i], a[i + j])
            if d < min_distance:
                min_distance = d
    return min_distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
