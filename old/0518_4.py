h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

print(h, w)
print(l)

l3 = []
for i in range(h):
    x = 0
    l2 = []
    for j in range(h):
        x += l[i][j]
        l2.append(x)
    l3.append(l2)

print(l3)


l5 = []
for i in range(w):
    x = 0
    l4 = []
    for j in range(w):
        x += l3[j][i]
        l4.append(x)
    l5.append(l4)

print(l5)