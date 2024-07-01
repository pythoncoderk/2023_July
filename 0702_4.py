n = list(input())
for i in range(len(n)):
    n[i] = int(n[i])


# print(n)

n = n[::-1]

x = 1
total = 0
for i in range(len(n)):
    total += n[i] * x
    if x == 1:
        x = 2
    else:
        x *= 2

print(total)