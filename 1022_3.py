x, y = map(int, input().split())
c = 0
while x <= y:
    x = int(x * 0.1) + x
    c += 1

print(c)