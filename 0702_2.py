n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

total = 0
p = 1
for i in range(n):
    total += abs(p - l[i])
    p = l[i]

print(total)