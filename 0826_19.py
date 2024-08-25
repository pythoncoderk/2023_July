n = int(input())

l = [int(input()) for i in range(n)]

max_l = l[0]
for i in l:
    max_l = max(max_l, i)

print(max_l)