n = int(input())
x = n
for i in range(9):
    if i == 8:
        print(n)
    else:
        print(n, end=" ")
        n = n + x