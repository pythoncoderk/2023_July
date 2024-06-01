l = list(map(int, input().split()))
l2 = []
count = 0
for a in range(4):
    for b in range(4):
        if b != a:
            for c in range(4):
                if c != a and c != b:
                    d = 6 - a - b - c

                    x = (l[a] * 10) + l[b] + (l[c] * 10) + l[d]
                    l2.append(x)

print(l2)

print(max(l2))