h, w = map(int, input().split())
dy, dx = map(int, input().split())

# print(h, w)
# print(dy, dx)

dy = abs(dy)
dx = abs(dx)
print((dy * w) + (dx * h) - (dy * dx))