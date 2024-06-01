n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l2 = []
l3 = []
x = 0
while l:
    if len(l) == 1:
        if l[0] == x+1:
            x = l[0]
            l3.append(l[0])
            l2.append(l3)
        else:
            if len(l) == 1:
                l2.append(l)
                l = []
            else:
                l2.append(l3)
                l2.append(l2)
    elif l[0]+1 == l[1]:
        x = l[0]
        l3.append(l.pop(0))
    else:
        x = l[0]
        l3.append(l.pop(0))
        l2.append(l3)
        l3 = []
# print(l2)

l4 = [len(i) for i in l2]
# print(l4)

max_l = max(l4)
index_l = l4.index(max_l)

print(l2[index_l][0], l2[index_l][-1])