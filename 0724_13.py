n, k = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    l[i] = l[i - 1] + l[i]

for i in range(k):
    x, y = map(int, input().split())
    x1 = l[x - 1]
    y1 = l[y]
    print(y1 - x1)



