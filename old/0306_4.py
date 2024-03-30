a, b = map(int, input().split())

n = 1
ans = 0

while True:
    if n >= b:
        print(ans)
        exit()
    n += a - 1
    ans += 1