l = [
    [6, 5, 4, 3, 2, 1],
    [3, 1, 8, 8, 1, 3]
]

for i in range(2):
    for j in range(6):
        if j == 5:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")