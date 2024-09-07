h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                print(y, x)