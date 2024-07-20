n, k = map(int, input().split())
d = {}
for _ in range(n):
    x, y, z = input().split()
    d[x] = [y, int(z)]

for _ in range(k):
    x1, x2, x3 = input().split()
    if d[x1][0] == x2:
        d[x1][1] -= int(x3)

keys = d.keys()

print(keys)

for _ in range(n):
    print(keys[_], d[keys[_][1]])