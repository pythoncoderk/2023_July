n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = set(l)
l2 = list(l2)

l3 = []
for i in range(len(l2)):
    count = 0
    for j in range(n):
        if l2[i] == l[j]:
            count += 1
    l3.append(count)
# print(l3)

max_l = max(l3)
for i in range(len(l3)):
    if l3[i] == max_l:
        print(l2[i])
        break