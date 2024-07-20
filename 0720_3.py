n, k = map(int, input().split())

d = {}
for _ in range(n):
    x, y, z = input().split()
    d[x] = [y, int(z)]

for _ in range(k):
    x1, y1, z1, = input().split()
    a, b = d[x1]
    if a != y1:
        continue
    d[x1] = (a, b - int(z1))

for c, e in d.items():
    print(c, e[])