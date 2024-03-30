a, b = map(int, input().split())


def chk(x):
    l = []
    l.append(x % 2)
    x //= 2
    return l

print(chk(a))