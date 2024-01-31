import re

n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
# print(n, m)
# print(l)

for i in range(m):
    l_x = []
    for j in range(n):
        x = l[j][i]
        if re.fullmatch("[0-9]|[0-9][0-9]|[1][0][0]", x) != None:
            l_x.append(int(l[j][i]))
    if sum(l_x) == 0:
        print(0)
    else:
        total = sum(l_x) // len(l_x)
        print(total)
