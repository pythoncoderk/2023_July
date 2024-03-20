import math

n, s, p = map(int, input().split())
x = math.ceil(n / s)
l = []
for i in range(x):
    l2 = []
    for j in range(1, s+1):
        if (i * s) + j > n:
            break
        else:
            l2.append((i * s) + j)
    l.append(l2)

if len(l) < p:
    print("none")
else:
    print(*l[p-1])