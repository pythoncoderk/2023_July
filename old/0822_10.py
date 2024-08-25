n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        if j == i - 1:
            print(j + 1)
        else:
            print(j + 1, end=" ")

