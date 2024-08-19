n, k = map(int, input().split())
d = {}

for _ in range(n):
    x, y, z = input().split()
    d[x] = [y, int(z)]

for _ in range(k):
    x1, y1, z1 = input().split()
    if d[x1][1] == y1:
        d[x1][2] -= int(z1)

print(d)