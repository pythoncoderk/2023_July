a, b, c = map(int, input().split())


def ha(a, b):
    c = a & b
    s = a ^ b
    return (c, s)


cx, sy = ha(a, b)
cy, s = ha(sy, c1)
c2 = cx ^ cy

print(c2, s)

