import copy
import re

a, b = map(int, input().split())
l = [str(i) for i in range(a, b+1)]
# print(l)
counts = 0
for i in l:
    x = copy.copy(i)
    y = re.fullmatch(r"([0]|[1]|[8]|[6]|[9])*", i)
    z = x.replace("6", "$")
    z = z.replace("9", "#")
    z = z.replace("$", "9")
    z = z.replace("#", "6")
    z = z[::-1]
    if z == i and y != None:
        # print(x)
        # print(y)
        counts += 1
print(counts)