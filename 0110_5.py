h, w, x, y = map(int, input().split())
l = [list(map(str, input().split())) for i in range(h)]
print(l)

x -= 1
y -= 1

for i in range(1, h):
    if 0 <= x - 1 < h:
        if l[x-i][y] == "#":
            break
        else:
            ans +=1
