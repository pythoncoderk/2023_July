import math

n = int(input())
l = [list(map(int, input().split())) for i in range(3)]

# print(n)
# print(l)

total = []
for i in range(3):
    x = sum(l[i])
    total.append(x)
print(math.prod(total))