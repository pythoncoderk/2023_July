l = list(map(int, input().split()))
l[2] = l[2]-1
l[3] = l[3]-1
lx = []
for i in range(l[0]):
    lx.append(list(input()))

if lx[l[2]][l[3]] == "#":
    print("Yes")
else:
    print("No")