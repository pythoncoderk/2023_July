n = int(input())

d = {}
s = set()

for _ in range(n):
    l = input().split()
    if l[1] == "give":
        name = l[0]
        money = int(l[2])
        if name not in d:
            d[name] = money
        else:
            d[name] += money
    else:
        s.add(l[0])

# print(d)
# print(s)

for a, b in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(a)

for c in sorted(s):
    print(c)