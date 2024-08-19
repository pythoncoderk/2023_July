n, m = map(int, input().split())
l = list(map(int, input().split()))

count = 0
for i in l:
    if i == m:
        count += 1

print(count)