def test(x):
    if x == 1:
        return 1
    return 1 + test(x - 1)

print(test(100))