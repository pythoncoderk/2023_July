def base_conversion(n, b):
    l = []
    while n >= b:
        l.append(str(n%b))
        n = n // b
    l.append(str(n))
    return ''.join(l[::-1])

print(base_conversion(18278, 26))

