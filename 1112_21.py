n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = []
for i in range(n):
    if l[i] >= m:
        l2.append(l[i])
print(min(l2))