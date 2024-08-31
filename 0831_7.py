a, b = map(int, input().split())

x = a - b

y = b - a

if (a - b) % 2 == 0:
    z = (a - b) // 2
else:
    z = x

ans = [x, y, z]
ans = set(ans)



print(len(ans))