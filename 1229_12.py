import math

n = int(input())
m = math.log2(n)
x = math.ceil(m)

if m == x:
    print("OK")
else:
    print("NG")
