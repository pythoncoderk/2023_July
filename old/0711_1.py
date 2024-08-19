a, b = map(str, input().split())


x = len(a)
y = len(b)
c = max(x, y)

d = a.zfill(c)
e = b.zfill(c)

total = ""
for i in range(c):
    h = d[i]
    k = e[i]
    f = int(h) + int(k)
    g = str(f)[-1]
    total += g

print(total)