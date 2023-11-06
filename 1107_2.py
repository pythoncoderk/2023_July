n = int(input())
l = [int(input()) for i in range(n)]
l2 = []
for i in range(n):
    for j in range(i):
        l2.append([l[i], l[j]])
l_f = []
while len(l2) != 0:
    if len(l_f) == 0:
        l_f.append([l2[0][0], l2[0][1]])
        del (l2[0])
    else:
        if abs(l_f[0][0] - l_f[0][1]) > abs(l2[0][0] - l2[0][1]):
            l_f = []
            l_f.append([l2[0][0], l2[0][1]])
            del(l2[0])
        else:
            del (l2[0])
if l_f[0][0] > l_f[0][1]:
    print(l_f[0][1])
    print(l_f[0][0])
else:
    print(l_f[0][0])
    print(l_f[0][1])