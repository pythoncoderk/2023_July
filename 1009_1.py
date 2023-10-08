for i in range(9):
    for j in range(9):
        if (j + 1) == 9:
            print((i + 1) * (j + 1))
        else:
            print((i + 1) * (j + 1), end=" ")