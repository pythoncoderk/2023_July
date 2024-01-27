n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(n, m)
# print(l)
xxx = 0
l_x = []
for i in range(n):
    l_y = []
    for j in range(n):
        l_y.append(l[j][i])
        xxx += 1
    l_x.append(l_y)

# print(l_x)

l = l_x

root = []
for i in range(n):
    x = []
    for j in range(n):
        if l[i][j]>= m:
            x.append(1)
        else:
            x.append(0)
    if sum(x) == 0:
        root.append(i+1)
if root == []:
    print("wait")
else:
    print(*root)
