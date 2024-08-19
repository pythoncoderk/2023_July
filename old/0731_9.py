n, m = map(int, input().split())
for i in range(n):
    x = int(input())
    print("{: >{}}".format(x, m))