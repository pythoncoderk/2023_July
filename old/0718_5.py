n, k = map(int, input().split())
d = {x: y for x, y in [input().split() for _ in range(n)]}
l = [list(map(str, input().split())) for _ in range(k)]

print(n, k)
print(d)
print(l)

