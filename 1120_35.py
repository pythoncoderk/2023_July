n = list(input())
n = list(map(int, n))
n.reverse()
x = 0
y = 2
for i in range(len(n)):
    if i == 0:
        x += n[i] * 1
    else:
        x += n[i] * (y)
        y *= 2
print(x)
