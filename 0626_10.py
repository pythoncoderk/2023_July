l = list(map(str, input().split()))
l2 = []
l3 = []

for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])
        l3.append(l.count(l[i]))

for i in range(len(l2)):
    print(l2[i], l3[i])

