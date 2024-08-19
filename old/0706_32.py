l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

x = abs(l[3] - l[4])
y = abs(l[4] - l[5])

x2 = abs(l2[3] - l2[4])
y2 = abs(l2[4] - l2[5])

z = abs(l[0] - l[1])
aa = abs(l[1] - l[2])

z2 = abs(l2[0] - l2[1])
aa2 = abs(l2[1] - l2[2])

print("Yes" if x == x2 and y == y2 and z == aa and z2 == aa2 else "No")