n = int(input())
l = list(map(int, input().split()))
k = int(input())
counts = 0

for i in l:
    if i == k:
        counts += 1

print(counts)