n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    if l[i] not in l2:
        l2.insert(0, l[i])
    else:
        index_l = 0
        for j in range(len(l2)):
            if l[i] == l2[j]:
                index_l = j
        l2.pop(index_l)
        l2.insert(0, l[i])

for i in range(len(l2)):
    print(l2[i])