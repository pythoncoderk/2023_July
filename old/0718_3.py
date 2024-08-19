n, k = map(int, input().split())
d = {x: y for x, y in [input().split() for i in range(n)]}

for i in range(k):
    x = input().split()
    if x[0] == "join":
        num, id = x[1], x[2]
        d[num] = id
    elif x[0] == "leave":
        num = x[1]
        del d[num]
    else:
        num = x[1]
        print(d[num])