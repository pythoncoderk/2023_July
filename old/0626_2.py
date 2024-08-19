l = list(map(str, input().split()))

l2 = []
for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])

# print(l2)

l3 = []
for i in range(len(l2)):
    l3.append(l.count(l2[i]))

for i in range(len(l2)):
    print(l2[i], l3[i])