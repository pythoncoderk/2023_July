l = list(map(str, input().split()))
# print(l)
x = l.index("x")

if x == 0:
    if l[1] == "+":
        print(int(l[4]) - int(l[2]))
    else:
        print(int(l[4]) + int(l[2]))
elif x == 2:
    if l[1] == "+":
        print(int(l[4]) - int(l[0]))
    else:
        print((int(l[4]) - int(l[0])) * -1)
else:
    if l[1] == "+":
        print(int(l[0]) + int(l[2]))
    else:
        print(int(l[0]) - int(l[2]))