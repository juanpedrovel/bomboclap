# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0   
    #Changes value to value / unit
    for i in range(len(values)):
        values[i] = values[i] / weights[i] 

    kvalue = sorted(range(len(values)), key=lambda k: values[k], reverse=True)

    for i in kvalue:
        if weights[i] >= capacity:
            value += capacity * values[i]
            break
        else:
            value += weights[i] * values[i]
            capacity -= weights[i]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))