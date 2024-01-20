import re

s = input()
s = re.sub("A","1", s)
s = re.sub("B","2", s)
s = re.sub("C","3", s)

# print(s)

l = [int(s[i]) for i in range(len(s))]

# print(l)
out = 0

if l[0] == 1:
    for j in range(len(l)-1):
        if l[j+1] == l[j] or l[j+1]-1 == l[j]:
            pass
        else:
            out += 1
else:
    out += 1

if l.count(2) == len(l):
    out = 0
elif l.count(3) == len(l):
    out = 0

if out == 0:
    print("Yes")
else:
    print("No")