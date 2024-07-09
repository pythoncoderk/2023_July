a, b = map(int, input().split())

x = abs(a - b)

min_l = a if a < b else b

print(abs((x // 2) + min_l) if x % 2 == 0 else "IMPOSSIBLE")