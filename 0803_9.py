n, m = map(int, input().split())
d = {}
for i in range(n):
    x, y = input().split()
    d[x] = int(y)

for i in range(m):
    x = input()
    if x not in d:
        print(-1)
    else:
        print(d[x])