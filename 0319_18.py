n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
l = sorted(l, key=lambda k: k[1])

for i in range(n):
    print(*l[i])