n = int(input())
x = 0
while n >= 2:
    if n % 2 == 0:
        x += 1
        n = n / 2
    else:
        break
print(x)

