n, a, x, y = map(int, input().split())

# print(n, a, x, y)

k = 0
total = 0
while k < n:
    if k < a:
        total += x
        k += 1
    else:
        total += y
        k += 1
print(total)