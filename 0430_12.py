m, n = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = [list(map(int, input().split())) for i in range(n)]

# print(m, n)
# print(l)
# print(l2)

total = []
for i in range(n):
    x = 0
    for j in range(m):
        x += (l[j] * l2[i][j]) // 100
    print(x)
