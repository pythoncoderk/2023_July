import re

s = input()
s2 = input()

l_s = list(s2)

l = []
for i in range(len(s)):
    x = re.search(s[i], s2)
    y = x.start()
    l.append(y + 1)
    l_s[y] = "*"
    s2 = "".join(l_s)

l.sort()
print(*l)
