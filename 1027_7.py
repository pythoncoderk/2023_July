l = [
    [1, 3, 5, 7],
    [8, 1, 3, 8]
]
for i in range(2):
    for j in range(4):
        if j == 3:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")