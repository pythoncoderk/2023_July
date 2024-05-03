import math

n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l2 = l[::]
l3 = []
for i in range(n):
    x = l2.pop(i)+1
    y = l2[::]
    for j in range(n-1):
        l2[j] -= 1
        l2.append(x)
        l3.append(math.prod(l2))
        l2 = y[::]
    l2 = l[::]
print(max(l3))