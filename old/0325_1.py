import math

l = list(map(int, input().split()))

x = math.ceil(l[0] / l[1])
print(x * l[2])