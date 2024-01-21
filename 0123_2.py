n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(l)

capslocks = 0

for i in range(n):
    if len(l[i]) == 2:
        print(l[i][1].upper(), end="")
    elif l[i][0] == "capslock":
        if capslocks == 0:
            capslocks = 1
        else:
            capslocks = 0
    else:
        if capslocks == 0:
            print(l[i][0], end="")
        else:
            print(l[i][0].upper(), end="")