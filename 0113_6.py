n = int(input())
l = list(map(int, input().split()))
k = int(input())
count_l = 0
for i in range(n):
    if l[i] == k:
        print(i+1)
        count_l += 1

