n = int(input())
l = [input() for i in range(n)]
l2 = []
for i in range(n):
    if l[i].count(".") != 3:
        l2.append(False)
    else:
        l2.append(l[i])
print(l2)
l3 = []
l3_s = []
for i in range(n):
    x = 0
    if l2[i] != False:
        l3_s.append(list(map(int, l2[1].split("."))))
        for j in range(4):
            if l2[i][j] >= 0 and l2[i][j] <= 255:
                pass
            else:
                x += 1
        if x >= 1:
            l3.append(False)
    else:
        l3.append(l2[i])
print(l3_s)
