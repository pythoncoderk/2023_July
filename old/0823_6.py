n = int(input())

ans = 0
for i in range(2, n + 1):
    prime_num = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime_num = False
            break
    if prime_num:
        ans += 1
print(ans)