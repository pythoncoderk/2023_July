p, q, r = map(int, input().split())
ab = {}
for i in range(p):
    x, y = map(int, input().split())
    ab[x] = y
bc = {}
for i in range(q):
    x, y = map(int, input().split())
    bc[x] = y

print(ab)
print(bc)

