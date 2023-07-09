import itertools
def is_odd(num):
    return num % 2 == 1

numbers = [10, 20, 31, 11, 3, 4]
for value, group in itertools.groupby(numbers, is_odd):
    print(f"{value}: {list(group)}")

