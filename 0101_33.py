n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(n)
# print(l)
capslock = 0
for i in range(n):
    if l[i][0] == "shift":
        print(l[i][1].upper(), end="")
    elif l[i][0] == "capslock":
        if capslock == 0:
            capslock = 1
        else:
            capslock = 0
    else:
        if capslock == 0:
            print(l[i][0], end="")
        else:
            print(l[i][0].upper(), end="")