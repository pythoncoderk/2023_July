n = int(input())

count = 0
while n != 0:
    if n >= 500:
        x = n % 500
        y = n // 500
        count += y
        n = x
    if n >= 100:
        x = n % 100
        y = n // 100
        count += y
        n = x
    if n >= 50:
        x = n % 50
        y = n // 50
        count += y
        n = x
    if n >= 10:
        x = n % 10
        y = n // 10
        count += y
        n = x
    if n >= 5:
        x = n % 5
        y = n // 5
        count += y
        n = x
    if n >= 1:
        x = n % 1
        y = n // 1
        count += y
        n = x
print(count)