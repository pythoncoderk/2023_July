import math

n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

max_l = max(l)
min_l = min(l)

for i in range(n):
    if l[i] == max_l:
        l.pop(i)
        break

for i in range(len(l)):
    if l[i] == min_l:
        l.pop(i)
        break

final = sum(l) / len(l)

print(math.floor(final * 10) / 10)