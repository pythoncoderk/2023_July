h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
n = int(input())
l2 = [list(map(int, input().split())) for i in range(n)]

print(h, w)
print(l)
print(n)
print(l2)

l3 = []
for i in range(h):
    x = 0
    l4 = []
    for j in range(w):
        l4.append(x + l[i][j])
        x += l[i][j]
    l3.append(l4)

l5 = []
for i in range(h):
    l4 = []
    x = 0
    for j in range(w):
        l4.append(l3[j][i] + x)
        x += l3[j][i]
    l5.append(l4)

l6 = []
for i in range(h):
    l7 = []
    for j in range(w):
        l7.append(l5[j][i])
    l6.append(l7)

print(l6)

for i in range(n):
    for j in range(len(l2[i])):
        l2[i][j] -= 1

print(l2)

for i in range(n):
    print(l6[l2[i][0] - 1][l2[i][1] - 1] + l6[l2[i][2]][l2[i][3]] - l6[0][l2[i][3]] - l6[l2[i][2]][0])
