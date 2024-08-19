a, b, c = map(int, input().split())

x = a - b

print(c - x if c - x > 0 else 0)