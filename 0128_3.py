l = list(map(str, input().split()))
l2 = l[::]
# print(l)
l3 = []
while l2:
    x = l2.pop(0)
    if l3.count(x) == 0:
        l3.append(x)
# print(l3)

for i in range(len(l3)):
    print(f"{l3[i]} {l.count(l3[i])}")