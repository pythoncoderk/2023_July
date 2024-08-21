n, k = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

max_l = 0
for i in range(n):
    for j in range(k):
        max_l = max([max_l, l[i][j]])

print(max_l)