x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

for i in range(x):
    for j in range(y):
        if l[i][j] == 0:
            pass
        else:
            a = i+1
            b = j+1

print(f"{a} {b}")