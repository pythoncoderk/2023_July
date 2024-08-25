n, k = map(int, input().split())

for i in range(k):
    l = []
    for j in range(1, n + 1):
        l.append(j)
    print(*l)