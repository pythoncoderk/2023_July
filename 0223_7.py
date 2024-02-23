import math

n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)
max_l = math.prod(l)
for i in range(n):
    for j in range(n-1):
        l2 = l[::]
        l2_pop = l2.pop(i)
        l2_pop += 1
        l2[j] -= 1
        l2.append(l2_pop)
        x = math.prod(l2)
        if max_l < x:
            max_l = x
print(max_l)
