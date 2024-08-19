a, b, c = map(int, input().split())

x = a ^ b
y = x and c
z = x and c

print(z, y)