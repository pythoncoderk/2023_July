n, a, b = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(abs(l[a-1][0] - l[b-1][0]) + abs(l[a-1][1] - l[b-1][1]))
