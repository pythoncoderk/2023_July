H, W = map(int, input().split())
h, w = map(int, input().split())

l = []
for i in range(H):
    l2 = []
    for j in range(W):
        l2.append(1)
    l.append(l2)

for i in range(h):
    for j in range(W):
        l[i][j] = 0

for i in range(H):
    for j in range(w):
        l[i][j] = 0

count = 0
for i in range(H):
    for j in range(W):
        if l[i][j] == 1:
            count += 1

print(count)