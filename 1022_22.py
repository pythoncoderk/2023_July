x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
for i in range(y):
    for j in range(x):
        if j == x-1:
            print(l[j][i])
        else:
            print(l[j][i], end=" ")
