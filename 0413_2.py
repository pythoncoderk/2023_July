n = int(input())
l = []
for i in range(n):
    l2 = []
    for j in range(int(input())):
        l2.append(list(map(int, input().split())))
    l.append(l2)

# print(l)

l3 = []
com = []
for i in range(n):
    count_l = 0
    for j in range(len(l[i])):
        l4 = []
        for k in range(l[i][j][0], l[i][j][0]+l[i][j][1]):
            if k not in l3:
                l4.append(k)
        if l[i][j][0]+l[i][j][1] - l[i][j][0] == len(l4):
            for ii in range(len(l4)):
                l3.append(l4[ii])

            com.append(i)
com = len(set(com))
print(com)

