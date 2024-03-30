import re

n = int(input())
l = [input() for i in range(n)]
# print(l)

for i in range(n):
    x = re.fullmatch("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", l[i])
    if x is not None:
        print("True")
    else:
        print("False")

