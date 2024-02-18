h, w, x, y = map(int, input().split())
l = [list(input()) for i in range(h)]
# print(h, w, x, y)
# print(l)

x -= 1
y -= 1
count = 1
for i in range(h):
    if l[x-(i+1)][y] == "#" or x - (i+1) < 0:
        break
    else:
        count += 1

for i in range(h):
    if l[x+(i+1)][y] == "#" or x + (i+1) > h:
        break
    else:
        count += 1

for i in range(w):
    if l[x][y-(i+1)] == "#" or y - (i+1) < 0:
        break
    else:
        count += 1

for i in range(w):
    if y + (i+1) > w:
        break
    else:
        if l[x][y+(i+1)] == "#":
            break
        else:
            count += 1
print(count)

