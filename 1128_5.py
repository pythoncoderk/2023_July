import re

n = int(input())
l = [input() for i in range(n)]
# print(n)
# print(l)
for i in range(n):
    x = re.fullmatch("([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])\."
                     "([\d][\d][\d]|[\d][\d]|[\d])\.([\d][\d][\d]|[\d][\d]|[\d])", l[i])
    if x != None:
        print(True)
    else:
        print(False)
