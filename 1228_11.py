x, y, z = map(int, input().split())

x1 = x * (y * 0.01)
x2 = x * (z * 0.01)

print(int(x2 - x1))