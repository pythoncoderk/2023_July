a, b, c = map(int, input().split())

x_1 = a ^ b
x_2 = a & b
y_1 = x_1 ^ c
y_2 = x_1 & c
f = x_2 ^ y_2

print(f, y_1)