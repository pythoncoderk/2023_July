n = int(input())


for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
    x = 2 ** i
    y = n % x
    print((n // x) % 2, end="")
