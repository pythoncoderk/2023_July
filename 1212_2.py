s = "ssgsdgdsjdkhfjsdkfhsadgfasdh flsdfh;osid"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for i in s:
    d.setdefault(i, 0)
    d[i] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)

for  i in s:
    d[i] += 1
print(d)
print(d["f"])