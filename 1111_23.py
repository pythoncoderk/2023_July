n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]

for i in range(n):
    l[i].append(0)

for i in range(m):
    for j in range(n):
        if l2[i][0] == l[j][0]:
            l[j][1] = int(l[j][1]) + int(l2[i][1])

l = sorted(l, reverse=True, key=lambda x: x[1])
for i in range(n):
    print(l[i][1])
