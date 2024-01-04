a, b = map(int, input().split())

def one(a, b):
    x = a ^ b
    return x

def two(a, b):
    y = a & b
    return y

print(f"{two(a, b)} {one(a, b)}")



