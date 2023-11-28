import math
import re

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    if re.search(r"[3]", l[i][0]) != None:
        x = int(l[i][1])
        l2.append(math.floor(x * 0.03))
    elif re.search(r"[5]", l[i][0]) != None:
        x = int(l[i][1])
        l2.append(math.floor(x * 0.05))
    else:
        x = int(l[i][1])
        l2.append(math.floor(x * 0.01))
print(sum(l2))