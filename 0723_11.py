n, k = map(int, input().split())
d = {input(): [] for i in range(n)}

print(n, k)
print(d)

for _ in range(k):
    a, b, c = input().split()
    d[a].append([b, c])

print(d)

for key, val in d.items():
    print(key)
    for b, c in val:
        print(b, c)
    print("-----")


