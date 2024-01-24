n = int(input())
m = n
n = (n * (n - 1)) // 2
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
l1 = []
for i in range(m):
    l_x = []
    for j in range(m):
        if i == j:
            l_x.append("-")
        else:
            l_x.append("*")
    l1.append(l_x)
# print(l1)
for i in range(n):
    l[i][0] = l[i][0] - 1
    l[i][1] = l[i][1] - 1
# print(l)

for i in range(n):
    l1[l[i][0]][l[i][1]] = "W"
# print(l1)

for i in range(m):
    for j in range(m):
        if l1[i][j] == "*":
            l1[i][j] = "L"
for i in range(m):
    print(*l1[i])