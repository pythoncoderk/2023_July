import itertools
def odd(n):
    return n % 2 == 1 # 奇数だった場合にはTrueが返る

l = [i for i in range(1, 11)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x, y in itertools.groupby(l, odd):
    print(f"{x}: {list(y)}")
