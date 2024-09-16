n, l = map(int, input().split())
l2 = list(map(int, input().split()))

l3 = []
for i in l2:
    if i >= l:
        l3.append(i)

if not l3:
    m = 0
else:
    m = max(l3)

print(sum(l2) - m + (m // 2))



