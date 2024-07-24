n = int(input())

d = {}
s = set()

for _ in range(n):
    l = input().split()
    name = l[0]
    status = l[1]
    if status == "give":
        money = int(l[2])
        if name not in d:
            d[name] = [money, name]
        else:
            d[name] = [money + d[name][0], name]
    else:
        s.add(name)

for name, money in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(name)

for _ in sorted(s):
    print(_)
