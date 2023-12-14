import math
import re

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    x = re.search(r"[5]|[3]", str(l[i][0]))
    if x is None:
        x_search = 0
    else:
        x_search = x.group()
    if x_search == "8":
        l2.append(math.floor(l[i][1] * 0.05))
    elif x_search == "9":
        l2.append(math.floor(l[i][1] * 0.03))
    else:
        l2.append(math.floor(l[i][1] * 0.01))
print(sum(l2))
