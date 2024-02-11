h, w = map(int, input().split())
l = [list(input()) for i in range(h)]
l2 = [list(map(int, input().split())) for i in range(h)]
# print(h, w)
# print(l)
# print(l2)
total = 0
for i in range(h):
    for j in range(w):
        if l[i][j] == "o":
            total += l2[i][j]
print(total)