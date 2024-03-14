n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

total = 0
for i in range(n):
    total += l[i]

print(total)
