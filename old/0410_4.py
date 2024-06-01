n, m = map(int, input().split())

l = [int(input()) for i in range(n-1)]

# print(n, m)
# print(l)

total = 0
for i in range(n-1):
    if l[i] <= m:
        total += l[i]
print(total)