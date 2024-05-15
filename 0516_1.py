l = [i for i in range(2, 51)]

print(l)

l5 = []
l2 = l[::]
while l2:
    l3 = []
    x = l2.pop(0)
    l5.append(x)
    for i in range(len(l2)):
        if l2[i] % x != 0:
            l3.append(l2[i])
    l2 = l3
print(l5)
