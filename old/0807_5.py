total = 0
for i in range(3):
    x, y = map(int, input().split())
    total += x * (y / 10)

print(int(total))