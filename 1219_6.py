n = int(input())
l = list(map(int, input().split()))
m = int(input())
counts = 0
for i in l:
    if i == m:
        counts += 1
print(counts)