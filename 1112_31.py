l = list(map(str, input().split()))
l2 = []
while l != []:
    x = l[0]
    y = l.count(x)
    l2.append([x, y])
    counts = 0
    while l.count(x) != 0:
        if l[counts] == x:
            l.pop(counts)
        else:
            counts += 1
for i in range(len(l2)):
    print(f"{l2[i][0]} {l2[i][1]}")

