a, b = map(int, input().split())
if a > b:
    max_s = a
    min_s = b
else:
    max_s = b
    min_s = a

print(f"{max_s} {min_s}")