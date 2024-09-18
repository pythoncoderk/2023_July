from decimal import Decimal, ROUND_HALF_UP

n, m = map(int, input().split())
x, y = map(int, input().split())

for i in range(m):
    z = int(input())
    a = abs(x - z)
    b = abs(y - z)
    print(x if a < b else y)


