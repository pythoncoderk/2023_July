import itertools
ite_chain = itertools.chain(["A", "B", "C"], "XYZ", range(1, 6))
for i in ite_chain:
    print(i, end="")