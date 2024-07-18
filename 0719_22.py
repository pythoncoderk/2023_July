n, k, p = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.append(p)

for _ in range(k):
    x = input().split()
    if x[0] == "join":
        l.append(int(x[1]))
    else:
        l.sort()
        print(l.index(p) + 1)