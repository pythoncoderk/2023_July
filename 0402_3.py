n = int(input())

l = list(map(int, input().split()))

max_index = 0
max_l = l[0]
for i in range(n):
    if l[i] > max_l:
        max_index = i
        max_l = l[i]

print(max_index)