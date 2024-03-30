l, r = map(int, input().split())

x = l + (r - l) / 3
y = r - (r - l) / 3

print(x, y)