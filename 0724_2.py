n = int(input())

d = {}
s = set()

for _ in range(n):
    l = input().split()
    name = l[0]
    st = l[1]
    if st == "give":
        if name not in d:
            d[name] = int(l[2])
        else:
            d[name] += int(l[2])
    else:
        s.add(name)

for a, b in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(a)

for _ in sorted(s):
    print(_)
