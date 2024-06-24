n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)


l2 = [l.count(l[i]) for i in range(n)]

# print(l2)

max_l = max(l2)

l3 = []
for i in range(n):
    if l2[i] == max_l:
        l3.append(l[i])

# print(l3)

l4 = set(l3)
l4 = list(l4)
l4.sort()

print(*l4)