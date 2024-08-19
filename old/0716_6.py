y, m, d = map(int, input().split())
a, b = map(int, input().split())

# print(y, m, d)
# print(a, b)

yer = False
count = 0
while True:
    if y % 4 == 1:
        yer = True
    if m % 2 == 0:
        d += 1
        count += 1
        if d >= 16:
            m += 1
            d = 1
    else:
        d += 1
        count += 1
        if d >= 14:
            m += 1
            d = 1
    if m >= 14:
        y += 1
        m = 1
    if y % 4 == 1 and m == a and d == b:
        break
print(count)
