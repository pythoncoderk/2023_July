a, b, c1 = map(int, input().split())

def ha(a, b):
    a1 = a & b
    b1 = a ^ b

    return a1, b1


f1, f2 = ha(a, b)

f3, f4 = ha(f2, c1)

print(f1, f3)

