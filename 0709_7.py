l = [1, 2, 3, 4, 5]
iterator = iter(l)
try:
    l1 = next(iterator)
    print(l1)
    l2 = next(iterator)
    print(l2)
    l3 = next(iterator)
    print(l3)
    l4 = next(iterator)
    print(l4)
    l5 = next(iterator)
    print(l5)
    l6 = next(iterator)
    print(l6)
except StopIteration:
    print("ループが終了します。")

print(dir(iterator))

[

    '__class__',
    '__delattr__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__iter__',
    '__le__',
    '__length_hint__',
    '__lt__',
    '__ne__',
    '__new__',
    '__next__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__setstate__',
    '__sizeof__',
    '__str__',
    '__subclasshook__'

]
