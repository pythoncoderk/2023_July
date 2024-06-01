import math

k, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(k)]

# print(k, n)
# print(l)

for i in range(k):
    if l[i][0] <= 0:
        x = (l[i][1] / n) * 100
        if 80 <= x <= 100:
            print("A")
        elif 70 <= x <= 79:
            print("B")
        elif 60 <= x <= 69:
            print("C")
        elif 0 <= x <= 59:
            print("D")
    else:
        x = (l[i][1] / n) * 100
        if 1 <= l[i][0] <= 9:
            x = math.floor(x * 0.8)
            if 80 <= x <= 100:
                print("A")
            elif 70 <= x <= 79:
                print("B")
            elif 60 <= x <= 69:
                print("C")
            elif 0 <= x <= 59:
                print("D")
        else:
            print("D")
