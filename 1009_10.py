n = int(input())
for i in range(n):
    x, y = input().split()
    x = float(x)
    y = int(y)
    print("{:.{}f}".format(x, y))