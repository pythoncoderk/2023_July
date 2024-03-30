y, m, d = map(int, input().split())
a, b = map(int, input().split())

print(y, m, d)
print(a, b)

next_y = y
while True:
    next_y += 1
    if next_y % 4 == 1:
        break
print(next_y)

print(next_y, a, b)

