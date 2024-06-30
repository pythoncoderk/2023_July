n = int(input())
l = [list(map(int, input().split())) for i in range((n * (n - 1)) // 2)]

# print(n)
# print(l)

for i in range((n * (n - 1)) // 2):
    l[i][0] = l[i][0] - 1
    l[i][1] = l[i][1] - 1

# print(l)

l2 = []
for i in range(n):
    l3 = []
    for j in range(n):
        l3.append("-")
    l2.append(l3)

# print(l2)

for i in range((n * (n - 1)) // 2):
    l2[l[i][0]][l[i][1]] = "W"
    l2[l[i][1]][l[i][0]] = "L"

# print(l2)

for i in range(n):
    print(*l2[i])