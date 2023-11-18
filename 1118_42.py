import re

n = int(input())
l = [input() for i in range(n)]
l2 = []
for i in l:
    x = re.fullmatch(r"([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])",i)
    if x != None:
        l2.append(True)
    else:
        l2.append(False)
for i in l2:
        print(i)
