a, b, c1 = map(int, input().split())

def halfAdder(a, b):
    c = a & b
    s = a ^ b
    return (c, s)

cx, sy = halfAdder(a, b)
cy, s = halfAdder(sy, c1)
c2 = cx ^ cy

print(c2, s)
