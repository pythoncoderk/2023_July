x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(3)]
print(l[x-1][y-1])