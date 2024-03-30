n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    l[i][1] = int(l[i][1])

l2 = [i for i in range(1, 101)]

# print(n)
# print(l)
# print(l2)
x = 999
l_f = []
for i in range(n):
    y = 0
    while y != x:
        x = len(l2)
        if l[i][0] == ">":
            if l2[y] > l[i][1]:
                l_f.append(l2[y])
                y += 1
            else:
                y += 1
        elif l[i][0] == "<":
            if l2[y] < l[i][1]:
                l_f.append(l2[y])
                y += 1
            else:
                y += 1
        else:
            if l2[y] % l[i][1] == 0:
                l_f.append(l2[y])
                y += 1
            else:
                y += 1
    l2 = l_f
    l_f = []
print(l2[0])

