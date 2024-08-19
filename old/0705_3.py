n, m = map(int, input().split())
l = list(map(int, input().split()))

# print(n, m)
# print(l)

count = 0
while l:
    x = l.pop(0)
    if m - x >= 0:
        m -= x
        count += 1
    else:
        break

print(count)