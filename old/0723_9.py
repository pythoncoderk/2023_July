n, k = map(int, input().split())
d = {input(): [] for i in range(n)}

print(n, k)
print(d)

for i in range(k):
    a, b, c = input().split()
    d[a] = [b, c]

print(d)