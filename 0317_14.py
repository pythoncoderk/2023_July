n, k, a = map(int, input().split())

p = a

while k > 0:
    if p > n:
        p = 0
    k -= 1
    p += 1
if p > n:
    p = 1
print(p)

