n, k = map(int, input().split())
l = []
x = 64
for i in range(26):
    x += 1
    for j in range(n):
        l.append(chr(x))

print(l[k-1])