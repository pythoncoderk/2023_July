n, q = map(int, input().split())
l = [input() for i in range(n)]

for i in range(q):
    x = input()
    if x in l:
        print(l.index(x) + 1)
    else:
        print(-1)