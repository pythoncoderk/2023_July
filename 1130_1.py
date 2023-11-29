from decimal import Decimal, ROUND_HALF_UP

x, y, z = map(int, input().split())
l = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(y)]
# print(x, y, z)
# print(l)
# print(l2)
l4 = []
for i in range(y):
    l3 = []
    for j in range(x):
        l3.append(l[j] * l2[i][j])
    l4.append(Decimal(str(sum(l3))).quantize(Decimal("1."), rounding=ROUND_HALF_UP))
l4.sort(reverse=True)
for i in range(z):
    print(l4[i])