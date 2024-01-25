a, b = map(int, input().split())
print(a, b)
counts1 = 0
while a == 0 or b == 0:
    a -= 1
    b -= 1
    counts1 += 1
