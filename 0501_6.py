y, m, d = map(int, input().split())
a, b = map(int, input().split())

# print(y, m, d)
# print(a, b)

y2 = y
while y2 % 4 != 1:
    y2 += 1

count = 0
while True:
    if y == y2 and m == a and d == b:
        # print(y, m, d)
        # print(y2, a, b)
        break
    else:
        if m % 2 == 0:
            d += 1
            count += 1
            if d >= 16:
                d = 1
                m += 1
                if m >= 14:
                    m = 1
                    y += 1
        else:
            d += 1
            count += 1
            if d >= 14:
                d = 1
                m += 1
                if m >= 14:
                    m = 1
                    y += 1

print(count)