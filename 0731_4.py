n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    print("{:.{}f}".format(x, int(y)))