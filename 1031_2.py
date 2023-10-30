n = int(input())
for i in range(9):
    if i == 8:
        print((i + 1) * n)
    else:
        print((i+1) * n, end=" ")