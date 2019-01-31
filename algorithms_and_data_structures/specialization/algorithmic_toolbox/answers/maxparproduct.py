# Uses python3

n = int(input())
a = [int(x) for x in input().split()]

number1 = 0
number2 = 0

for i in range(n):
    if a[i] >= number1:
        number2 = number1
        number1 = a[i]
    elif a[i] > number2:
        number2 = a[i]

print (number1 * number2)
