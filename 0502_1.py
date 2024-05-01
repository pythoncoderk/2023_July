k, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(k)]

# print(k, n)
# print(l)

for i in range(k):
    x = (l[i][1] / n) * 100
    if 1 <= l[i][0] <= 9:
        x = int(0.8 * x)
    elif l[i][0] >= 10:
        x = 0
    if 0 <= x <= 59:
        print("D")
    elif 60 <= x <= 69:
        print("C")
    elif 70 <= x <= 79:
        print("B")
    else:
        print("A")