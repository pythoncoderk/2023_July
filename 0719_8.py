n, k = map(int, input().split())
l = [input() for _ in range(n)]
d = {i: l[i] for i in range(n)}

print(n, k)
print(d)

for _ in range(k):
    x = input().split()
    g = d.get(x[1])
    print(g)

