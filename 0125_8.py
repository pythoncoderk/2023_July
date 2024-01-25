h, w = map(int, input().split())
dy, dx = map(int, input().split())

print(h, w)
print(dy, dx)

print((dx * h) + (dy * w) - (dy * dx))