n, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    if 1 in l[i]:
        for j in range(len(l[i])):
            if l[i][j] == 1:
                print(i + 1, j + 1)