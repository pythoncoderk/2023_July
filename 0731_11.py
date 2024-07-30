n, a, b = map(int, input().split())

for i in range(n):
    if i == n - 1:
        print(f"({a}, {b})")
    else:
        print(f"({a}, {b})", end=", ")