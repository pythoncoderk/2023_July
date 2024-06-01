n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    if l[i][0] not in l2:
        l2.append(l[i][0])
# print(l2)

l3 = []
for i in range(len(l2)):
    R = 0
    L = 0
    for j in range(n):
        if l2[i] == l[j][0]:
            if l[j][1] == "R":
                R += 1
            else:
                L += 1
    l3.append([l2[i], R, L])
# print(l3)

f_count = 0
for i in range(len(l3)):
    if l3[i][1] != 0 and l3[i][2] != 0:
        if l3[i][1] == l3[i][2]:
            f_count += l3[i][2]
        elif l3[i][1] > l3[i][2]:
            f_count += l3[i][2]
        else:
            f_count += l3[i][1]
print(f_count)