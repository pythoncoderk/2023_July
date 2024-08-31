n = int(input())
l = [input().split() for i in range(n)]

# print(n)
# print(l)

lef = None
rig = None
ans = 0
for i in range(n):
    if l[i][1] == "L":
        if lef is not None:
            ans += abs(int(l[i][0]) - lef)
            lef = int(l[i][0])
        else:
            lef = int(l[i][0])
    else:
        if rig is not None:
            ans += abs(int(l[i][0]) - rig)
            rig = int(l[i][0])
        else:
            rig = int(l[i][0])

print(ans)
