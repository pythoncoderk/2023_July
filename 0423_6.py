h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

# print(h, w)
# print(l)

for i in range(h):
    l2 = []
    for j in range(w):
        if l[i][j] >= 128:
            l2.append(1)
        else:
            l2.append(0)
    print(*l2)