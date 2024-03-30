m, n = map(int, input().split())

l = []
for i in range(1, m):
    for j in range(1, n):
        l.append([i, j])
# print(l)

count = 0
for i in range(len(l)):
    x = 0
    if 3 in l[i] and 4 in l[i]:
        x += 1
    if x >= 1:
        count += 1
    y = 0
    if 6 in l[i] and 8 in l[i]:
        y += 1
    if y >= 1:
        count += 1
    z = 0
    if 12 in l[i] and 16 in l[i]:
        z += 1
    if z >= 1:
        count += 1

print(count)