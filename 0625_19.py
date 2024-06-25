import math
from decimal import *

n, m = map(int, input().split())

l = [int(input()) for i in range(m)]

diff = math.ceil(n / 2)

# print(diff)

for i in range(m):
    if l[i] < n:
        print(n)
    else:
        x = l[i] % n
        if x >= diff:
            print(((l[i] // n) * n) + n)
        else:
            print((l[i] // n) * n)
