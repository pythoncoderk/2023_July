h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

print(h, w)
print(l)
print(q)
print(l2)

l3 = []
for i in range(h):
    l4 = []
    x = 0
    for j in range(w):
        x += l[i][j]
        l4.append(x)
    l3.append(l4)

l5 = []
for i in range(h):
    l4 = []
    x = 0
    for j in range(w):
        x += l3[j][i]
        l4.append(x)
    l5.append(l4)
print(l5)

l6 = []
for i in range(h):
    l4 = []
    for j in range(w):
        l4.append(l5[j][i])
    l6.append(l4)

l_in = [0] * w
l6.insert(0, l_in)

for i in range(h):
    l6[i].insert(0, 0)


print(l6)
print(l2)

for i in range(q):
    x = l6[l2[i][2]][l2[i][3]]
    y = l6[l2[i][0] - 1][l2[i][1] - 1]
    a_x = l6[0][l2[i][3]]
    a_y = l6[l2[i][3]][0]
    print(x + y - a_x - a_y)