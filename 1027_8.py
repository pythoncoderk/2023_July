n = int(input())
l = []
for i in range(5):
    l.append(list(map(int, input().split())))
for i in range(5):
    for j in range(n):
        if j == n-1:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")