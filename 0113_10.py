n = int(input())
l = list(map(int, input().split()))

counts_l = 0

for i in range(n):
    if l[i] % 2 == 0:
        counts_l = i + 1
        break
print(counts_l)