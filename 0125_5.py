n = int(input())
l = [int(input()) for i in range(n)]
# print(l)
total = 0
total_l = 0
start = 1
for i in range(n):
    if start > l[i]:
        total = start - l[i]
        total_l += total
        start = l[i]
    else:
        total = l[i] - start
        total_l += total
        start = l[i]
print(total_l)