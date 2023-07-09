import itertools
li = list(range(10))
print(li)

islice_object = itertools.islice(li, 5)
print(islice_object)
print(list(islice_object))