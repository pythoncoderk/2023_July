l = [list(map(int, input().split())) for i in range(4)]
x = 4
counts = 0
counters = 10
for i in range(4):
    for j in range(x):
        if l[i][j] == 1:
            counts = counters
            counters -= 1
        else:
            counters -= 1
    x -= 1
print(counts)
print(sum(map(sum, l)))