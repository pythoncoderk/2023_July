n = int(input())

ans = ""
while n > 0:
    x = n // 2
    ans = str(n % 2) + ans
    n = x

print(ans)
