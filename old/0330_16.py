a, b, c, d = map(int, input().split())

l = [(i * c) + (b - i) * d for i in range(1, b)]
l2 = [[i, b - i] for i in range(1, b)]

if l.count(a) >= 2:
    print("miss")
elif l.count(a) == 1:
    xx = l.index(a)
    print(*l2[xx])
else:
    print("miss")

