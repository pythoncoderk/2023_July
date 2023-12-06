n = int(input())
l = list(map(int, input().split()))
k = int(input())
l2 = []
for i in l:
    if i <= k:
        l2.append(i)
print(max(l2))