n = int(input())

total = 0
while True:
    x = n % 10
    if x != 0:
        total += x
        n //= 10
    else:
        break

print(total)
