n, v = map(int, input().split())
l = list(map(int, input().split()))

count = 0
for i in range(n):
    if l[i] == v:
        count += 1

print(count)