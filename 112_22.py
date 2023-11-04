x, y, z = map(int, input().split())
a = x * (y / 100)
b = x * (z / 100)
print(int(b - a))