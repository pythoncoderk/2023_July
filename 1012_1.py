x, y = map(int, input().split())
l = [input() for i in range(x)]
l2 = [input() for j in range(y)]

for i in range(y):
    if l2[i] in l:
        print(l.index(l2[i])+1)
    else:
        print(-1)
