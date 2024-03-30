m, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]

# print(m, n)
# print(l)

l2 = []
for i in range(m-n+1):
    total = 0
    l2_l = []
    for j in range(i, n+i):
        if j == i:
            l2_l.append(l[i][0])
            total += l[j][1]
        elif j == n+i-1:
            l2_l.append(l[j][0])
            total += l[j][1]
        else:
            total += l[j][1]
    l2_l.append(total)
    l2.append(l2_l)

# print(l2)
if n >= 2:
    l_f = sorted(l2, reverse=False, key=lambda x: (x[2], x[0]))
    print(l_f[0][0], l_f[0][1])
else:
    l_f = sorted(l2, reverse=False, key=lambda x: (x[0]))
    print(l_f[0][0], l_f[0][0])

