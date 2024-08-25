import itertools

l = [0, 0, 0, 0, 0, 1]

x = itertools.groupby(l)
for i, j in x:
    print(f"{i}: {list(j)}")