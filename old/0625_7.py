l = list(map(str, input().split()))

l2 = []
for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])

for i in range(len(l2)):
    print(l2[i])

for i in range(len(l2)):
    print(1)

