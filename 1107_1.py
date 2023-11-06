n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

l2 = []
for i in range(n):
    if l[i][0] == 'out':
        if len(l2) == 0:
            pass
        else:
            l2.pop(0)
    else:
        l2.append(l[i][1])
for i in l2:
    print(i)
