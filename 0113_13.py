n = int(input())
l = list(map(int, input().split()))
k = int(input())

l2 = [i for i in l if i <= k]
# print(l2)

max_l = l2[0]
for i in l2:
    if max_l < i:
        max_l = i
print(max_l)