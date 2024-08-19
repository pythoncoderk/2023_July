t = int(input())


def fanc(x):
    return x ** 2 + 2 * x + 3


print(fanc(fanc(fanc(t) + t) + fanc(fanc(t))))