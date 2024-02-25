n, m = map(int, input().split())
l = []
for i in range(n, n+(m * 10), m):
    l.append(i)
print(*l)