import re

n, s = map(str, input().split())
l = list(map(str, input().split()))


def changes(x, y):
    xx = y.index(x)
    yy = chr(xx + 97)
    return yy


for i in range(int(n)):
    for j in range(len(l[i])):
        k = changes(l[i][j], s)
        l[i] = re.sub(l[i][j], k, l[i])
