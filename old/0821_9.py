n = int(input())

i = 1
count = 0
while n >= i:
    if n % i == 0:
        count += 1
        i += 1
    else:
        i += 1

print(count)
