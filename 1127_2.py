n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(m)]
# print(n, m)
for i in range(len(l)):
    l[i][0] = int(l[i][0])
# print(l)
l2 = []
for i in range(1, n+1):
    l3 = []
    counts = 0
    for j in range(len(l)):
        if i % l[j][0] == 0:
            l3.append(l[j][1])
            counts += 1
    if counts == 0:
        l3.append(i)
    l2.append(l3)
# print(l2)
for i in range(len(l2)):
    for j in range(len(l2[i])):
        if j == len(l2[i])-1:
            print(l2[i][j])
        else:
            print(l2[i][j], end=" ")