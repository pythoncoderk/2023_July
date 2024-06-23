a = int(input())

x = 1
y = 1

l = []
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i + j == a:
            l.append([i, j])

# print(l)

max_l = 0
for i in range(len(l)):
    x = l[i][0] * l[i][1]
    if max_l < x:
        max_l = x

print(max_l)