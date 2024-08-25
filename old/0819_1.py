import itertools

l = [1, 2, 3, 4, 5]
x = itertools.accumulate(l)

print(list(x))

