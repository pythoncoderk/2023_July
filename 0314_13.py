import math

n = int(input())
l = list(map(int, input().split()))

l_max = max(l)
l_min = min(l)

for i in range(n):
    if l[i] == l_max:
        l.pop(i)
        break

for i in range(len(l)):
    if l[i] == l_min:
        l.pop(i)
        break

total = sum(l) / len(l)
print(round(total, 1))
