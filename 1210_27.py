m,n = map(int, input().split())
l = []
for i in range(10):
    l.append(m)
    m += n
print(*l)