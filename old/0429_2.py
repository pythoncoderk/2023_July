l = list(map(int, input().split()))

# print(l)
l2 = []
x = 0
y = 0
for a in range(4):
    for b in range(4):
        if b != a:
            for c in range(4):
                if c != a and c != b:
                    d = 6 - a - b - c
                    x = (l[a] * 10) + l[b]
                    y = (l[c] * 10) + l[d]
                    l2.append(x + y)

print(max(l2))