x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
# print(x, y)
# print(l)
l2 = []
xxx = 0
for i in range(3):
    l3 = []
    for j in range(x):
        l3.append(l[j][xxx])
    l2.append(l3)
    xxx += 1
for i in range(len(l2)):
    l2[i].sort()
for i in range(len(l2)):
    l2[i] = l2[i][:2]
for i in range(len(l2)):
    l2[i] = max(l2[i])
# print(l2)
final = []
for i in range(x):
    counts = 0
    for j in range(3):
        if l[i][j] <= l2[j]:
            counts += 1
    final.append(counts)
for i in final:
    print(i)