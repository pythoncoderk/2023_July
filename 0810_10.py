n = int(input())
l = [list(input()) for i in range(n)]

# print(n)
# print(l)

l2 = l[::-1]
# lll = max(l2)
# print(l2)

x = 0
l3 = []
l4 = []
while True:
    while x != n:
        if len(l2[x]) != 0:
            xx = l2[x].pop(0)
            l3.append(xx)
            x += 1
        else:
            l3.append("*")
            x += 1

    l4.append(l3)
    l3 = []
    x = 0
    total = 0
    for i in range(len(l2)):
        total += len(l2[i])
    if total == 0:
        break

for i in range(len(l4)):
    xxx = "".join(l4[i])
    for i in range(len(xxx)):
        if xxx[-1] == "*":
            xxx = xxx[:-1]
        else:
            print(xxx)
            break