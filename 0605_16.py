n, x, t = map(int, input().split())

count = 0
while n > 0:
    n -= x
    count += 1

print(count * t)

