n = list(input())
for i in range(len(n)):
    n[i] = int(n[i])
n.reverse()
# print(n)
total = 0
x = 2
for i in range(len(n)):
    if i == 0:
        total += 1 * n[i]
    else:
        total += x * n[i]
        x *= 2
print(total)