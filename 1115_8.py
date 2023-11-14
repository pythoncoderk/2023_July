n, m = map(int, input().split())
x = n ^ m
y = n and m
print(f"{y} {x}")