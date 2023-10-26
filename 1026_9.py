x, y = map(int, input().split())

c = x & y
s = x ^ y

print(c, s)
