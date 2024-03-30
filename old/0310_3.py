import math

a, b = map(int, input().split())
if a % b == 0:
    print(math.floor(a / b))
    exit()
else:
    print(math.ceil(a / b))