a, b, c = map(int, input().split())

x = int(b / a)

print(x if x < c else c)