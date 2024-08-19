l = [[1, 3, 5, 7], [8, 1, 3, 8]]

for i in range(len(l)):
    for j in range(len(l[i])):
        if j == len(l[i]) - 1:
            print(l[i][j])
        else:
            print(l[i][j], end=" ")