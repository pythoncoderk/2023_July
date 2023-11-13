n, m = map(int, input().split())
l = [n]
for i in range(9):
    l.append(n + m)
    n = n + m

for i in range(10):
    if i == 9:
        print(l[i])
    else:
        print(l[i], end=" ")