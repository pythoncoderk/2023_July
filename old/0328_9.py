h, w = map(int, input().split())
dy, dx = map(int, input().split())

# print(h, w)
# print(dy, dx)

print((abs(dx * h)) + (abs(dy * w)) - (abs(dy * dx)))