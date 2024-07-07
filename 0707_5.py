l = list(map(int, input().split()))
l.sort()

total = 0
for i in range(len(l) - 1):
    total += abs(l[i + 1] - l[i])

print(total)