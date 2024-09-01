n = int(input())
l = [input() for i in range(n)]
l.sort()
d = {l[i]: 0 for i in range(n)}

m = int(input())
for i in range(m):
    x, y = input().split()
    d[x] += int(y)

for i in range(n):
    print(d[l[i]])

