x, y = map(int, input().split())
l = []
for i in range(x):
    l.append(list(map(int, input().split())))
for i in range(x):
    for j in range(y):
        if j == y-1:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")