n, p, q, r, s = map(int, input().split())
l = list(map(int, input().split()))
# print(l)

x = [l[i] for i in range(p-1, q)]
y = [l[i] for i in range(r-1, s)]

# print(x)
# print(y)

a = 0
for i in range(r-1, s):
    l[i] = x[a]
    a += 1

b = 0
for i in range(p-1, q):
    l[i] = y[b]
    b += 1

print(*l)