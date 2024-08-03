n, q = map(int, input().split())
d = {}
for i in range(n):
    yy = input()
    if yy not in d:
        d[yy] = i + 1

# print(d)

for i in range(q):
    y = input()
    if y not in d:
        print(-1)
    else:
        print(d[y])