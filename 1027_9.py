n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    for j in range(5):
        if j == 4:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")