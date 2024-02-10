import math

k, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(k)]

# print(k, n)
# print(l)

for i in range(k):
    x = (l[i][1] / n) * 100
    if l[i][0] >= 10:
        x = 0
    elif 1 <= l[i][0] <= 9:
        x = math.floor(x * 0.8)

    if 80 <= x <= 100:
        print("A")
    elif 70 <= x <= 79:
        print("B")
    elif 60 <= x <= 69:
        print("C")
    else:
        print("D")