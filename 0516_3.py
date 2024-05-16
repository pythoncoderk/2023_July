w, h = map(int, input().split())
t = []
for i in range(h):
    t.append(list(map(int, input().split())))

count = 0
for y in range(h):
    for x in range(w):
        if t[y][x] == 1:
            count += 1

print(count)