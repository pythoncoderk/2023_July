n = int(input())
l = [input() for i in range(n)]
x, y, z = 5, 3, 3
for i in range(n):
    print((ord(l[i][0]) - 95) % x + (ord(l[i][0]) - 95) % y + (ord(l[i][0]) - 95) % z)