h, w = map(int, input().split())
l = [input() for i in range(h)]

# print(h, w)
# print(l)

count = 0

for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            count += 1
print(count)