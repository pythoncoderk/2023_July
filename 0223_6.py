import math

n = int(input())
l = list(map(int, input().split()))
l.sort()
l[0] += 1
l[-1] -= 1

print(math.prod(l))