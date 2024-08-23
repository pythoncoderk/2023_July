n = int(input())

ans = 0
for i in range(1, n + 1):
    now = i
    while now % 2 == 0:
        now //= 2
        ans += 1

print(ans)