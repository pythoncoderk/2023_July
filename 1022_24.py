n = int(input())
l = [i+1 for i in range(n)]

prime = []
for i in range(2, 1001):
    x = 0
    for j in range(i):
        if x == 3:
            break
        elif i % (j+1) == 0:
            x += 1
    if x == 2:
        prime.append(i)
xxx = 0
for i in prime:
    if i <= n:
        xxx += 1
print(xxx)

