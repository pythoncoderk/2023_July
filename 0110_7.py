l = [input() for i in range(9)]

for i in range(3):
    l2 = []
    for j in range(3):
        l2.append(l.pop(0))
    print(*l2, end="\n")