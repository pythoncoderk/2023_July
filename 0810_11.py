q = int(input())
d = {}

for i in range(q):
    xy = input().split()
    if len(xy) == 2:
        x = int(xy[0])
        y = int(xy[1])
        if x == 1:
            if y in d:
                d[y] += 1
            else:
                d[y] = 1
        elif x == 2:
            d[y] -= 1
            if d[y] == 0:
                del d[y]
    else:
        print(len(d))

