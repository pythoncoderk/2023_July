n, k = map(int, input().split())
l = list(map(int, input().split()))

total = 0
for i in range(n):
    total += l[i] // k

print(total)