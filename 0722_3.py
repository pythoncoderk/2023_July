n, k = map(int, input().split())
d = {}
for _ in range(n):
    x, y, z = input().split()
    d[x] = [y, int(z)]

# print(d)

for _ in range(k):
    x, y, z = input().split()
    if d[x][0] == y:
        d[x][1] -= int(z)

# print(d)

for a, b in d.items():
    print(a, b[1])