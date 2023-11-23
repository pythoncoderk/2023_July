import re

a, b = map(str, input().split())
a1 = int(a)
b1 = int(b)
l = []
for i in range(a1, b1+1):
    l.append(str(i))
print(l)
counts = 0
for i in l:
    if len(i) == 1:
        if i == "1" or i == "8" or i == "0":
            counts += 1
    else:
        i2 = i[::-1]
        x = re.match(r"([0]|[1]|[8])*", i)
        if i == i2 and x != None:
            counts += 1
print(counts)
