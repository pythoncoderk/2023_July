import itertools
it1 = (1, 2, 3, 4, 5)
it2 = ["abc", "ABC", "123"]
for v in itertools.zip_longest(it1, it2):
    print(v)