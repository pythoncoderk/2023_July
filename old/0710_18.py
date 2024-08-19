n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    l2.append(l[i][0] + l[i][1])

l3 = []
for i in range(n):
    l3.append(l2.count(l2[i]))

# print(l2)
# print(l3)

max_l = max(l3)

l4 = []
for i in range(n):
    if l3[i] == max_l:
        l4.append(l2[i])

# print(l4)

l4 = set(l4)
l4 = list(l4)
l4.sort()

print(l4[0])