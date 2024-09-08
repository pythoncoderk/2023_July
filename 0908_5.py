h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

# print(h, w)
# print(l)

for i in range(h):
    for j in range(w):
        if j == 0 or l[i][j - 1] == "#":
            if j == w - 1 or l[i][j + 1] == "#":
                if i == 0 or l[i - 1][j] == "#":
                    if i == w - 1 or l[i + 1][j] == "#":
                        print(i, j)
