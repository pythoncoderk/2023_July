n = int(input())
x = 0
now2 = 0
while now2 <= n:
    now = 2 ** x
    now2 += now
    x += 1

print(x)