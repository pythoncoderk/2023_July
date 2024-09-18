h, w = map(int, input().split())
l = [list(input()) for i in range(h)]

# print(h, w)
# print(l)
# print(l[1][0])

for i in range(h):
    for j in range(w):
        if i == 0 or l[i - 1][j] == "#":
            if i == h - 1 or l[i + 1][j] == "#":
                print(i, j)

