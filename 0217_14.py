n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    l[i][1] = int(l[i][1])
# print(l)
l2 = sorted(l, key=lambda x: x[1])
for i in l2:
    print(*i)