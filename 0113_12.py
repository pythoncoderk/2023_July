n = int(input())
l = list(map(int, input().split()))
k = int(input())

counts_l = 0

l2 = [l[i] for i in range(n) if l[i] >= k]
# print(l2)
min_l = l2[0]
for i in l2:
    if min_l > i:
        min_l = i
print(min_l)