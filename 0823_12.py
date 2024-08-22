n, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(l)

for i in range(k):
    l2 = []
    for j in range(n):
        l2.append(l[j][i])
    print(*l2)