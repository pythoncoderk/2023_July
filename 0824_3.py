n = int(input())

ans = 0
for i in range(1, n + 1):
    now = i
    while True:
        if now % 2 == 0:
            ans += 1
            now //= 2
        else:
            break

print(ans)