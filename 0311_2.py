h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

# print(h, w)
# print(l)

for i in range(h):
    for j in range(w):
        if l[i][j] >= 128:
            l[i][j] = 1
        else:
            l[i][j] = 0
# print(l)

for i in l:
    print(*i)