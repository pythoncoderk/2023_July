n = int(input())
l = list(map(int, input().split()))
k = int(input())

count_l = 0

for i in range(n):
    if l[i] == k:
        count_l += i+1
        break

print(count_l)