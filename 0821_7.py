n = int(input())
l = list(map(int, input().split()))

max_l = 101
for i in range(n):
    max_l = min(max_l, i + 1 + l[i])

print(max_l)