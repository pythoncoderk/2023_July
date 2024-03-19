a, b, c = map(int, input().split())

x = a ^ b
y = a and b

print(y, x)

x1 = x ^ y
y1 = x and y

print(x1, y1)