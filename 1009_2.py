n = int(input())
for i in range(n):
    for j in range(n):
        if (j+1) % n == 0:
            print((i + 1) * (j + 1))
        else:
            print((i + 1) * (j + 1), end=" ")

