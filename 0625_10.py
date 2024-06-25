l = list(map(str, input().split()))

# print(l)

l2 = []
for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])

l3 = [l.count(l2[i]) for i in range(len(l2))]

# print(l2)
# print(l3)


for i in range(len(l2)):
    print(f"{l2[i]} {l3[i]}")