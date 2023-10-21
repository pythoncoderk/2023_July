n = list(input())
x = 0
while len(n) != 0:
    y = int(n[0])
    n.pop(0)
    x += y
print(x)