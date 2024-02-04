n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = []
for i in range(n):
    l3 = []
    for j in range(2):
        if j == 1:
            l3.append(int(l[i][j]))
        else:
            l3.append(l[i][j])
    l2.append(l3)
# print(n)
# print(l)
# print(l2)
chk = [i for i in range(1, 101)]
# print(chk)
for i in range(n):
    for j in range(len(chk)):
        if l[i][0] == ">":
            if chk[j] < l2[i][1]+1:
                chk[j] = 999
        elif l[i][0] == "<":
            if chk[j] > l2[i][1]-1:
                chk[j] = 999
        else:
            if chk[j] % l2[i][1] != 0:
                chk[j] = 999
# print(chk)
for i in chk:
    if i != 999:
        print(i)
