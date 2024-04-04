h, w = map(int, input().split())
l = [list(input()) for i in range(h)]
l2 = [list(map(int, input().split())) for i in range(h)]

# print(h, w)
# print(l)
# print(l2)

count = 0
for i in range(h):
    for j in range(w):
        if l[i][j] == "o":
            count += l2[i][j]
print(count)