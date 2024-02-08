l = list(map(str, input().split()))
l_x = l[::]
# print(l)
l2 = []
i = 0
while l_x:
    if l_x[i] in l2:
        l_x.pop(0)
    else:
        l2.append(l_x.pop(0))
# print(l2)
for i in range(len(l2)):
    print(f"{l2[i]} {l.count(l2[i])}")