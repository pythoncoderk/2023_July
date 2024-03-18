n = int(input())
m = n * (n-1) // 2

l = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    l[i][0] = l[i][0] - 1
    l[i][1] = l[i][1] - 1
# print(l)

l2 = [["-" for j in range(n)] for i in range(n)]
# print(l2)

for i in range(m):
    l2[l[i][0]][l[i][1]] = "W"
# print(l2)

for i in range(n):
    for j in range(n):
        if i != j and l2[i][j] != "W":
            l2[i][j] = "L"

for i in range(n):
    print(*l2[i])