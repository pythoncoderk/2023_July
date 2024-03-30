a, b = map(int, input().split())
l = [[j+1+i*3 for j in range(3)] for i in range(3)]
# print(l)

x1, y1 = 0, 0
x2, y2 = 0, 0

for i in range(3):
    for j in range(3):
        if l[i][j] == a:
            x1 = i
            y1 = j

for i in range(3):
    for j in range(3):
        if l[i][j] == b:
            x2 = i
            y2 = j
# print(x1, y1)
# print(x2, y2)

if (y1 - 1 == y2 or y1 + 1 == y2) and x1 == x2:
    print("Yes")
else:
    print("No")