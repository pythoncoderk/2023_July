n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]

for i in range(n):
    l[i][0] = int(l[i][0])

for i in range(k):
    l2[i][1] = int(l2[i][1])

d = dict(l)
#
# print(d)
# print(l2)

for i in range(k):
    if l2[i][0] == "call":
        if l2[i][1] in d:
            print(d[l2[i][1]])
    elif l2[i][0] == "leave":
        if l2[i][1] in d:
            d.pop(l2[i][1])
    else:
        d[l2[i][1]] = l2[i][2]

