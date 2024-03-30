m, n = map(int, input().split())

l = []
for i in range(1, 11):
    if i == 1:
        l.append(m)
    else:
        m += n
        l.append(m)
print(*l)