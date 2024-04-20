import timeit

print(timeit.timeit("[i for i in range(10)]"))

l = []
timeit.timeit("for i in range(10) l.append(i)")