import re

n = int(input())
l = [input() for i in range(n)]
for i in range(n):
    x = re.fullmatch(r"([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\."
                     r"([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])", l[i])
    if x != None:
        print(True)
    else:
        print(False)