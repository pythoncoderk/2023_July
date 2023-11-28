import sys

n = int(input())
l_a = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l_c = [list(map(str, input().split())) for i in range(m)]
# print(n)
# print(m)
for i in range(n):
    l_a[i][1] = int(l_a[i][1])
# print(l_a)
for i in range(m):
    l_c[i][1] = int(l_c[i][1])
# print(l_c)
d_c = {}
for i in range(m):
    d_c[l_c[i][0]] = l_c[i][1]
# print(d_c)

for i in range(n):
    tools_counts = 0
    for j in range(m):
        if l_c[j][0].count(l_a[i][0]) != 0:
            tools_counts += 1
    if tools_counts == 0:
        print(0)
        sys.exit()
x = 0
counts = 0
while min(d_c.values()) >= 0:
    if d_c[l_a[x][0]] - l_a[x][1] >= 0:
        d_c[l_a[x][0]] -= l_a[x][1]
        if x == n-1:
            x = 0
            counts += 1
        else:
            x += 1
    else:
        if x == n - 1:
            x = 0
            counts += 1
        else:
            break
print(counts)