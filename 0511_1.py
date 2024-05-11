h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

print(h, w)
print(l)
print(q)

for i in range(q):
    for j in range(len(l2[i])):
        l2[i][j] -= 1

print(l2)

l4 = []
for i in range(h):
    x = 0
    l3 = []
    for j in range(w):
        x += l[i][j]
        l3.append(x)
    l4.append(l3)

print(l4)

l6 = []
for i in range(h):
    x = 0
    l5 = []
    for j in range(w):
        x += l4[j][i]
        l5.append(x)
    l6.append(l5)

for i in range(len(l6)):
    l6[i].insert(0, 0)

print(l6)

for i in range(q):
    x = l6[l2[i][2]][l2[i][3]] + l6[l2[i][0]][l2[i][1]]
    y = l6[l2[i][1]][l2[i][2]] + l6[l2[i][0]][l2[i][3]]
    print(x - y)