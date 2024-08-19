def total(n):
    a = 0
    for i in range(1, n + 1):
        a += i
    return a

# print(total(10))

def total2(n):
    if n == 0:
        return 0
    return n + total2(n - 1)

print(total2(10))