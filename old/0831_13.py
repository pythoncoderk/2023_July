n = int(input())
l = [input() for i in range(n)]

m = int(input())
d = {}
for i in range(m):
    x, y = input().split()
    d[x] = int(y)

print(d)

ans = list(d.values())

print(ans)