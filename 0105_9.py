n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l2 = []
l3 = []
for i in range(n):
    if l[i][0] == 1:
        if l[i][1] == 1:
            l2.append(l[i][2])
        else:
            l3.append(l[i][2])
    elif l[i][0] == 2:
        if l[i][1] == 1:
            print(l2.pop(0))
        else:
            print(l3.pop(0))
    else:
        print(f"{len(l2)} {len(l3)}")