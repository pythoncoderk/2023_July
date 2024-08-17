n, a, b = map(int, input().split())

l = list(map(int, input().split()))

total = 0
for i in range(a - 1, b):
    total += l[i]

print(total)