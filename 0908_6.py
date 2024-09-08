h, w = map(int, input().split())
l = [list(input()) for _ in range(h)]

# print(h, w)
# print(l)

for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            print(i, j)
            break