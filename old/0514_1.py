import bisect

n, k = map(int, input().split())
l = list(map(int, input().split()))

print(n, k)
print(l)

l_a = k // 2
l_b = k - l_a

print(l_a)
print(l_b)

chk = False
while not chk:
    total = 0
    for i in range(n):
        total += l_a // l[i]

    if total == k:
        chk = True
    elif total < k:
        l_a += l_b // 2
    else:
        l_a // 2

