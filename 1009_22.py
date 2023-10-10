x, y = map(int, input().split())
l = list(map(int, input().split()))

for i in range(y):
    z = list(map(int, input().split()))
    if z[0] == 0:
        l.append(z[1])
    elif z[0] == 1:
        l.pop()
    elif z[0] == 2:
        for i in range(len(l)):
            if i+1 == len(l):
                print(l[i])
            else:
                print(l[i], end=" ")
