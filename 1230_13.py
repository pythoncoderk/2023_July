import math
import re

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
l2 = []
for i in range(n):
    if re.search(r"3", l[i][0]) is not None:
        l2.append(math.floor(l[i][1] * 0.03))
    elif re.search(r"5", l[i][0]) is not None:
        l2.append(math.floor(l[i][1] * 0.05))
    else:
        l2.append(math.floor(l[i][1] * 0.01))
print(sum(l2))