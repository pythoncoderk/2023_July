n, m, k, q = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

print(l[k - 1][q - 1])