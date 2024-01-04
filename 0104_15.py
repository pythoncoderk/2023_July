a, b, c = map(int, input().split())

x = a ^ b
y = a ^ b

final = y & c

print(f"{final} {x}")