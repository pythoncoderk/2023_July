l = list(map(int, input().split()))

total = 0
for i in range(len(l)):
    total += 7 - l[i]

print(total)