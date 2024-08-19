def factrial(n):
    if n == 1:
        return 1
    return n * factrial(n - 1)


print(factrial(8))