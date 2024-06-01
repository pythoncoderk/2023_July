n, k = map(int, input().split())
l = list(map(int, input().split()))

# print(n, k)
# print(l)

bus = 0
i = 0
count = 0
while n != i:
    if bus + l[i] <= k:
        bus += l[i]
        i += 1
    else:
        count += 1
        bus = l[i]
        i += 1
print(count + 1)
