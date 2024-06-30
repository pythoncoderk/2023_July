a, b, c = map(int, input().split())

count = 0
if a < b:
    a, b = b, a
while c > 0:
    c -= a
    count += 1

print(count)