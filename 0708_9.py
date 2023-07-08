gen = (i + 1 for i in range(1, 6))
print(gen)

list = [1, 2, 3]
gen = (i + 1 for i in list)
print(gen)

def func():
    for i in range(1, 6):
        yield i + 1

def func():
    for i in range(1, 6):
        return gen(i + 1)