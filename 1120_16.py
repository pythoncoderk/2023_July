import math

n = int(input())
l = [int(input()) for i in range(n)]
print(math.floor(sum(l)/n))