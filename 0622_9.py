a, d = map(int, input().split())

x = (a + 1) * d
y = (d + 1) * a

print(x if x >= y else y)