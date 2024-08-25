n = int(input())
l = list(map(int, input().split()))

max_l = 0
for i in range(len(l)):
    x = i + 1 + l[i]
    if max_l < x:
        max_l = x

print(max_l)