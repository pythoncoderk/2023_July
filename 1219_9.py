n = int(input())
l = list(map(int, input().split()))
k = int(input())
counts = 0
x = 1
for i in l:
    if i == k:
        counts = x
        x += 1
    else:
        x += 1
print(counts)