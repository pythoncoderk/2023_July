n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(m)]
for i in range(m):
    l[i][0] = int(l[i][0])

# print(n, m)
# print(l)

for i in range(1, n+1):
    l2 = []
    for j in range(m):
        if i % l[j][0] == 0:
            l2.append(l[j][1])
    if not l2:
        print(i)
    else:
        print(*l2)