l = list(map(str, input().split()))
for i in range(len(l)):
    if l[i].isdecimal():
        l[i] = int(l[i])
# print(l)

if l[0] == "x":
    if l[1] == "+":
        print(l[4] - l[2])
    else:
        print(l[4] + l[2])
elif l[2] == "x":
    if l[1] == "+":
        print(l[4] - l[0])
    else:
        print((l[4] - l[0]) * -1)
else:
    if l[1] == "+":
        print(l[0] + l[2])
    else:
        print(l[0] - l[2])