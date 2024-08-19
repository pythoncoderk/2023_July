n, k = map(int, input().split())
l = [input() for _ in range(n)]

for _ in range(k):
    x = input().split()
    if x[0] == "handshake":
        if l:
            l.sort()
            for _ in range(len(l)):
                print(l[_])
    elif x[0] == "join":
        l.append(x[1])
    else:
        y = l.index(x[1])
        del l[y]
