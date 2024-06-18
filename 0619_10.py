h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

# print(h, w)
# print(l)
# print(q)
# print(l2)

for i in range(h):
    x = 0
    for j in range(w):
        l[i][j] += x
        x = l[i][j]

for i in range(h):
    x = 0
    for j in range(w):
        l[j][i] += x
        x = l[j][i]

for i in range(h):
    l[i].insert(0, 0)

l_pulus = [0] * (w + 1)
l.insert(0, l_pulus)

# print(l)

for i in range(q):
    x_1 = l[l2[i][0] - 1][l2[i][1] - 1]
    y_1 = l[l2[i][2]][l2[i][3]]
    x_2 = l[l2[i][2]][l2[i][0] - 1]
    y_2 = l[l2[i][1] - 1][l2[i][3]]
    print(x_1 + y_1 - x_2 - y_2)

