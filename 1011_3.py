n = int(input())
l = [input() for i in range(n)]
l2 = list(set(l))
l2 = sorted(l2)
for i in range(len(l2)):
    print(f"{l2[i]} {l.count(l2[i])}")