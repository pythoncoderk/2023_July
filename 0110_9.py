h, w, x, y = map(int, input().split())
l = [list(input()) for i in range(h)]

print(h, w, x, y)
print(l)

x -= 1
y -= 1
counts = 0
while x >= 0:
    if l[x][y] == ".":
        counts += 1

