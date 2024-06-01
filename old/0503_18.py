n = int(input())

l = []
l2 = []
for i in range(n):
    l.append(int(input()))
    l3 = []
    for j in range(l[i]):
        l3.append(list(map(int, input().split())))
    l2.append(l3)

# print(l)
# print(l2)

l3 = []
l4 = []
l5 = []
for i in range(n):

    for j in range(l[i]):
        for q in range(l2[i][j][0], l2[i][j][0]+l2[i][j][1]):
            l4.append(q)
        chk = True
        for k in range(len(l4)):
            if l4[k] in l3:
                chk = False
        if chk == True:
            for ii in l4:
                l3.append(ii)
            l5.append(i)
        l4 = []

l5 = set(l5)
print(len(l5))


