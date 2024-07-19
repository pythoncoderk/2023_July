n, k = map(int, input().split())
s = {input() for _ in range(n)}

for _ in range(k):
    x = input().split()
    if x[0] == "join":
        s.add(x[1])
    elif x[0] == "leave":
        s.remove(x[1])
    else:
        for _ in sorted(s):
            print(_)
