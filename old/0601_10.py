n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)
# print(l2)

l3 = []
for i in range(m):
    l4 = []
    for j in range(n):
        l4.append(l2[j][i])
    l3.append(l4)

for i in range(m):
    l3[i].sort(reverse=True)

# print(l3)

chk = True
for i in range(m):
    if chk == False:
        print("No")
        exit()
    x = 0
    for j in range(n):
        x += l3[i][j]
        chk2 = True
        if x >= l[i]:
            break
        else:
            if j == n - 1:
                chk = False

if chk:
    print("Yes")
else:
    print("No")