n, k, a = map(int, input().split())
x = a
a -= 1
while k > 0:
    a += 1
    k -= 1
    if a > n:
        a = 1

print(a)
