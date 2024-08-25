n = int(input())

for i in range(1, n + 1):
    n *= i

print(n)

count = 0
while True:
    if n % 2 == 0:
        n //= 2
        count += 1
    else:
        break

print(count)