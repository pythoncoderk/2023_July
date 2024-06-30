a, b = map(int, input().split())

x = a // b
y = a % b

# print(x)
# print(y)

print(x if y == 0 else x + 1)