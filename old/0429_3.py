h, w = map(int, input().split())
dy, dx = map(int, input().split())

# print(h, w)
# print(dy, dx)

print(abs(dy * w) + abs(dx * h) - abs(dy * dx))