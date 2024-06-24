n, h = map(int, input().split())
l = list(map(int, input().split()))

count = 0
for i in range(n):
    if h >= l[i]:
        h -= l[i]
        count += 1
    else:
        break

print(count)