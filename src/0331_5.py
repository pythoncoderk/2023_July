k, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(k)]

print(k, n)
print(l)

for i in range(k):
    x = 1
    if l[i][0] > 0:
        if l[i][0] >= 10:
            x = 0
        else:
            x = 0.8
    y = n / l[i][1]
    z = x * y
    if 80 <= z <= 100:
        print("A")
    elif 70 <= z <= 79:
        print("B")
    elif 60 <= z <= 69:
        print("C")
    else:
        print("D")
