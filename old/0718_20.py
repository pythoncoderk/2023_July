n, k = map(int, input().split())
d = {x: y for x, y in [input().split() for _ in range(n)]}

for _ in range(k):
    x = input().split()
    if x[0] == "join":
        num, id = x[1], x[2]
        d[num] = id
    elif x[0] == "leave":
        del d[x[1]]
    else:
        print(d[x[1]])
