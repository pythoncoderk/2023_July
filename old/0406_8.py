n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)

for i in range(m):
    for j in range(3):
        if j != 2:
            l2[i][j] = l2[i][j]-1
# print(l2)

for i in range(m):
    if l[l2[i][0]] >= l2[i][2]:
        l[l2[i][0]] -= l2[i][2]
        l[l2[i][1]] += l2[i][2]
    else:
        l[l2[i][1]] += l[l2[i][0]]
        l[l2[i][0]] = 0
# print(l)

for i in l:
    print(i)