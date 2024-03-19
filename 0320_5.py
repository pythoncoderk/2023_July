n, k, a = map(int, input().split())

# print(n, k, a)

while k > 1:
    k -= 1
    a += 1
    if a > n:
        a = 1


print(a)