n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

for i in range(m):
    if l[l2[i][0] - 1] - l2[i][2] < 0:
        l[l2[i][1] - 1] += l[l2[i][0] - 1]
        l[l2[i][0] - 1] = 0
    else:
        l[l2[i][0] - 1] -= l2[i][2]
        l[l2[i][1] - 1] += l2[i][2]
for i in range(n):
    print(l[i])