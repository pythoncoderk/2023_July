a, b, c = map(int, input().split())
def test(a, b):
    x = a and b
    y = a ^ b
    return (x, y)

ax, bx = test(a, b)
cx, dx = test()