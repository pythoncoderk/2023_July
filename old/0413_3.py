import math

n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)
l3 = l[:]
l2 = []
for i in range(n):
    for j in range(n):
        if i != j:
            l3[i] += 1
            l3[j] -= 1
            l2.append(math.prod(l3))
            l3 = l[:]
print(max(l2))