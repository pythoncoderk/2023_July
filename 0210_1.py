y, m, d = map(int, input().split())
a, b = map(int, input().split())

# print(y, m, d)
# print(a, b)
y2 = y
while True:
    y2 += 1
    if y2 % 4 == 1:
        break

count = 0
while True:
    if str(y)+str(m)+str(d) == str(y2) + str(a) + str(b):
        break
    else:
        d += 1
        if m % 2 == 0:
            if d >= 16:
                d = 1
                m += 1
                count += 1
                if m >= 14:
                    m = 1
                    y += 1

            else:
                count += 1
        else:
            if d >= 14:
                d = 1
                m += 1
                count += 1
                if m >= 14:
                    m = 1
                    y += 1

            else:
                count += 1
print(count)


