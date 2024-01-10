a, b = map(int, input().split())

x = a ^ b
y = a & b

print(f"{y} {x}")