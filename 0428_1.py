import math

n, s, p = map(int, input().split())

# print(n, s, p)

l = []
x = 1
for i in range(math.ceil(n / s)):
    l2 = []
    for j in range(s):
        if x <= n:
            l2.append(x)
            x += 1
    l.append(l2)

if len(l) < p:
    print("none")
else:
    print(*l[p-1])
