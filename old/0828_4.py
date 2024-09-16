n, m, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m, k)
# print(l)

for i in range(n):
    count = 0
    for j in range(m):
        if l[i][j] == k:
            count += 1
    print(count)