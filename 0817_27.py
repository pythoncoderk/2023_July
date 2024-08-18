a, b, c = map(int, input().split())

l = []
if b > c:
    while b != c:
        l.append(b)
        b += 1
        if b > 24:
            b = 0
else:
    while b != c:
        l.append(b)
        b += 1
        if b > 24:
            b = 0

l.append(b)

print("Yes" if a not in l else "No")