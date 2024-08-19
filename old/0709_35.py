n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)

l2 = [l[i][0] - l[i][1] * 5 for i in range(n)]

for i in range(n):
    if l2[i] < 0:
        l2[i] = 0

# print(l2)

for i in range(n):
    if l2[i] >= m:
        print(i + 1)