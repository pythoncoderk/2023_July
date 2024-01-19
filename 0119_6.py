import math

n, k = map(float, input().split())
n = int(n)
l = [float(input()) for i in range(n)]

total_l = sum(l)
print(math.ceil(round(total_l / k, 2)))