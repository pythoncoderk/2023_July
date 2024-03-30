n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)


a = 0
b = 0
c = 0
d = 0

for i in range(n):
    if l[i][0] == 0:
        x = l[i][1]
        a += x
    elif l[i][0] == 1:
        x = l[i][1]
        b += x
    elif l[i][0] == 2:
        x = l[i][1]
        c += x
    else:
        x = l[i][1]
        d += x
a = (a // 100) * 5
b = (b // 100) * 3
c = (c // 100) * 2
d = (d // 100) * 1

print(a + b + c + d)