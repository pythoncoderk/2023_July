x, y, n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
print(l[n-1][m-1])