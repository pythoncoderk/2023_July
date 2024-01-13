n = int(input())
l = list(map(int, input().split()))
k = int(input())
count_l = 0
for i in l:
    if i == k:
        count_l += 1
print(count_l)
