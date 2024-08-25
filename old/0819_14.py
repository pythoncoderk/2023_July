n, m = map(int, input().split())

count = 0
while n > m - 1:
    if n % m == 0:
        n //= m
        count += 1
    else:
        break

print(count)