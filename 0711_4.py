n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
# print(n)
# print(l)

l2 = [i for i in range(1, 101)]

for i in range(n):
    if l[i][0] == ">":
        for j in range(len(l2)):
            if l2[j] == "*":
                pass
            elif l2[j] <= l[i][1]:
                l2[j] = "*"
    elif l[i][0] == "<":
        for j in range(len(l2)):
            if l2[j] == "*":
                pass
            elif l2[j] >= l[i][1]:
                l2[j] = "*"
    else:
        for j in range(len(l2)):
            if l2[j] == "*":
                pass
            elif l2[j] % l[i][1] != 0:
                l2[j] = "*"

for i in l2:
    if i != "*":
        print(i)
        break

