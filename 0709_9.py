import itertools
it = itertools.chain(["A", "B"], "abc", range(3))
for element in it:
    print(element)