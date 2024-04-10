n, m = map(int, input().split())
a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(a, b, c)
# print(l)

total = 0
for i in range(n):
    x = (l[i] * c) - a - (b * m)
    if x < 0:
        total += 1

print(total)