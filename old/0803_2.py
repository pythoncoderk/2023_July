n, q = map(int, input().split())
l = list(map(int, input().split()))

for i in range(q):
    x = list(map(int, input().split()))
    if x[0] == 0:
        l.append(x[1])
    elif x[0] == 1:
        l.pop()
    else:
        for i in range(len(l)):
            if i == len(l) - 1:
                print(l[i])
            else:
                print(l[i], end=" ")