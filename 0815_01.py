def max_3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(max_3(100, 200, 7))