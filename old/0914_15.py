x, y = map(int, input().split())

l = []
for i in range(y):
    a, b = map(str, input().split())
    l.append([int(a), b])

get_l = []
for i in range(y):
    if l[i][0] not in get_l and l[i][1] == "M":
        print("Yes")
        get_l.append(l[i][0])
    else:
        print("No")